#!/usr/bin/env python3
"""Extract data from ArmSoM (and similar) schematic PDFs without poppler.

Needs only PyMuPDF:  pip install pymupdf

Modes
-----
  --text [PAGE]        Dump plain text for all pages (or one page).
  --render PAGE OUT    Render a page to PNG (default 3x ~216 dpi; --zoom N).
  --connectors PAGE    Reconstruct 2-column connector pin->net tables from a
                       sheet by clustering pin-number tokens and snapping the
                       nearest net label in the correct x-band. Tweak the
                       --lx/--rx/--xband options if a sheet's geometry differs.

This is the tool used to build reference/cm1-*.md. Use it to extend the skill
to ArmSoM-CM1-IO-1V1_Sch.pdf or to re-verify after a schematic revision.
"""
import argparse, re, sys

try:
    import fitz  # PyMuPDF
except ImportError:
    sys.exit("PyMuPDF missing: pip install pymupdf")

NET = re.compile(r"^[A-Z][A-Z0-9_./]{2,}$")
XREF = re.compile(r"^\[[0-9,]+\]$")


def cy(w):
    return (w[1] + w[3]) / 2


def cx(w):
    return (w[0] + w[2]) / 2


def cmd_text(doc, page):
    pages = [page - 1] if page else range(doc.page_count)
    for i in pages:
        t = doc[i].get_text().strip()
        print(f"\n===== PAGE {i + 1} (chars={len(t)}) =====\n{t}")


def cmd_render(doc, page, out, zoom):
    pix = doc[page - 1].get_pixmap(matrix=fitz.Matrix(zoom, zoom))
    pix.save(out)
    print(f"saved {out} {pix.width}x{pix.height}")


def cmd_connectors(doc, page, lx, rx, xband, ytol):
    """Reconstruct connector pinouts on a sheet.

    lx/rx = x center of the left/right pin-number columns (the small integers
    printed at the connector body). xband = (min,max) x for net labels on each
    outer side. Net label is the one whose y is nearest the pin row.
    """
    words = doc[page - 1].get_text("words")
    pins = [w for w in words if re.fullmatch(r"\d{1,2}", w[4]) and 1 <= int(w[4]) <= 60]
    Lpin = [w for w in pins if lx - 4 <= cx(w) <= lx + 4]
    Rpin = [w for w in pins if rx - 4 <= cx(w) <= rx + 4]
    nets = [w for w in words if NET.match(w[4]) or XREF.match(w[4])]

    def label(pw, side):
        if side == "L":
            band = [w for w in nets if xband[0] <= cx(w) <= lx - 6]
        else:
            band = [w for w in nets if rx + 6 <= cx(w) <= xband[1]]
        if not band:
            return ""
        near = min(band, key=lambda w: abs(cy(w) - cy(pw)))
        if abs(cy(near) - cy(pw)) > ytol + 1:
            return ""
        row = sorted([w for w in band if abs(cy(w) - cy(near)) <= ytol], key=cx)
        name = " ".join(w[4] for w in row if NET.match(w[4]))
        xr = " ".join(w[4] for w in row if XREF.match(w[4]))
        return f"{name} {xr}".strip()

    # Connectors are separated vertically; cluster pin rows by y-gap.
    ys = sorted(cy(w) for w in Lpin + Rpin)
    if not ys:
        print("no pin-number tokens found near lx/rx; adjust --lx/--rx")
        return
    groups, cur = [], [ys[0]]
    for y in ys[1:]:
        if y - cur[-1] < 40:
            cur.append(y)
        else:
            groups.append(cur)
            cur = [y]
    groups.append(cur)
    for gi, g in enumerate(groups):
        ymin, ymax = min(g) - 5, max(g) + 5
        L = {int(w[4]): label(w, "L") for w in sorted(Lpin, key=cy) if ymin <= cy(w) <= ymax}
        R = {int(w[4]): label(w, "R") for w in sorted(Rpin, key=cy) if ymin <= cy(w) <= ymax}
        if not L and not R:
            continue
        npin = max(list(L) + list(R))
        print(f"\n#### connector group {gi + 1} (y {ymin:.0f}-{ymax:.0f})")
        for n in range(1, npin + 1, 2):
            print(f"{n:>3} {L.get(n,''):<36} | {n+1:>3} {R.get(n+1,'')}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pdf")
    ap.add_argument("--text", nargs="?", const=0, type=int, metavar="PAGE")
    ap.add_argument("--render", nargs=2, metavar=("PAGE", "OUT"))
    ap.add_argument("--zoom", type=float, default=3.0)
    ap.add_argument("--connectors", type=int, metavar="PAGE")
    ap.add_argument("--lx", type=float, default=252, help="left pin-number column x")
    ap.add_argument("--rx", type=float, default=332, help="right pin-number column x")
    ap.add_argument("--xband", type=float, nargs=2, default=(70, 600), help="net-label x range")
    ap.add_argument("--ytol", type=float, default=1.6)
    a = ap.parse_args()
    doc = fitz.open(a.pdf)
    if a.render:
        cmd_render(doc, int(a.render[0]), a.render[1], a.zoom)
    elif a.connectors:
        cmd_connectors(doc, a.connectors, a.lx, a.rx, tuple(a.xband), a.ytol)
    elif a.text is not None:
        cmd_text(doc, a.text)
    else:
        cmd_text(doc, 0)


if __name__ == "__main__":
    main()
