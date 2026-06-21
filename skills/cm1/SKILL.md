---
name: cm1
description: >-
  ArmSoM CM1 (RK3506J) system-on-module and CM1-IO carrier hardware reference.
  Pre-extracted schematic data so you never have to re-parse the ArmSoM PDFs:
  the J8001/J8002 board-to-board connector pinouts, power tree and rails, SoC
  voltage domains, boot-strap (SARADC_IN0) options, and per-peripheral net maps
  (FSPI flash, SDMMC/TF, MIPI-DSI panel, USB OTG0/1, RMII0/1, audio/SAI, FlexBUS).
  Use this whenever a task touches the ArmSoM CM1 module or CM1-IO board: pin
  assignment, "which connector pin is net X", device-tree pinmux, FlexBUS/QSPI
  external-bus wiring, display/backlight, power sequencing, GPIO offsets, or "what's on
  J8001/J8002". Trigger on "CM1", "CM1-IO", "ArmSoM", "RK3506", "J8001", "J8002",
  "FLEXBUS1", "core connector", or any question answerable from the CM1
  schematic. Prefer this skill over opening the PDF.
---

# ArmSoM CM1 / CM1-IO Hardware Reference

The ArmSoM **CM1** is an RK3506J (triple Cortex-A7 + Cortex-M0) system-on-module.
It mates to a carrier (the **CM1-IO** board, or a custom carrier) through two
board-to-board connectors, **J8001** (40-pin) and **J8002** (44-pin). This skill
holds the schematic data extracted from `ArmSoM-CM1-1V1_Sch.pdf` (rev V1.1,
2025-06-10) so design questions can be answered without re-rendering the PDF.

## How to use this skill

1. **Pin / net questions** → [reference/cm1-connectors.md](reference/cm1-connectors.md).
   This is the authoritative J8001/J8002 board-to-board pinout, the single most
   common lookup. Every net the carrier can reach is here.
2. **Power / rails / sequencing** → [reference/cm1-power.md](reference/cm1-power.md).
3. **SoC peripherals & voltage domains** (FSPI, SDMMC, MIPI-DSI, USB, RMII,
   audio, FlexBUS, boot strap) → [reference/cm1-peripherals.md](reference/cm1-peripherals.md).
4. **Module overview / block diagram** → [reference/cm1-overview.md](reference/cm1-overview.md).

When you cite a fact, name the source sheet (e.g. "CM1 sch sheet 16,
CORE-CONN-LED"). If the answer is *not* in these files, say so and only then
fall back to rendering the PDF with `scripts/extract_schematic.py`.

## Ground rules (read before changing pin assignments)

- **Connector net names are the SoC's default pad function**, often a `/`-mux
  label (e.g. `DSMC_D5/FLEXBUS1_D8`, `UART2_RX/PWM0_CH3_IR_RX`). The actual
  function depends on the RK3506 pinmux in the device tree — the silk/net name
  is not proof of how the pin is currently driven.
- **⚠ FlexBUS0 ≠ FlexBUS1 — `flexbus1_data` is INPUT-only, and the A-bank pins
  (`GPIO1_A0..A7` = `FLEXBUS1_D0..D7`) have NO `FLEXBUS0_*` alternate.** Do not
  assume the `FLEXBUS1_*` pins can be driven as a FlexBUS0 master (the silked
  J8002 "QSPI data" pins 1–4 cannot). A FlexBUS master (QSPI NOR, etc.) needs
  its data on the bidirectional `FLEXBUS0_D*` pads (B/C/D-bank). Full details +
  pad map + the on-hardware proof are in
  [reference/cm1-connectors.md](reference/cm1-connectors.md) (FlexBUS note).
- The `[n]` tag after a net is the **schematic sheet cross-reference** (the other
  sheet the net appears on), not a pin number.
- The CM1-IO carrier re-exposes most of these nets on its 40-pin and 44-pin
  user headers. This skill documents the board as designed — the SoC default
  net names and connector pinout — and intentionally does not encode any
  particular product's pin usage or device-tree choices.

## Regenerating / extending (CM1-IO next)

The extractor that built these tables is reusable:

```bash
python3 scripts/extract_schematic.py <pdf> --text                 # dump per-page text
python3 scripts/extract_schematic.py <pdf> --render <page> out.png # render a page
python3 scripts/extract_schematic.py <pdf> --connectors <page>     # reconstruct a 2-col connector
```

It needs only PyMuPDF (`pip install pymupdf`) — no poppler. The **CM1-IO**
carrier is covered by the sibling **`armsom:cm1-io`** skill.

## Source documents

| File | What it is | Rev |
|------|------------|-----|
| `ArmSoM-CM1-1V1_Sch.pdf` | CM1 module schematic, 17 sheets | V1.1 (2025-06-10) |
| `ArmSoM-CM1-IO-1V1_Sch.pdf` | CM1-IO carrier schematic (see `armsom:cm1-io`) | V1.1 (2025-06-10) |

CM1 sheet index: 1 Block Diagram · 2 Power Diagram · 3 SOC POWER/GND ·
4 SOC OSC/PLL/PMUIO · 5 SOC DRAM Controller · 6 SOC Flash Controller ·
7 SOC USB/ACODEC/SARADC · 8 SOC VOP/LCDC mux · 9 SOC RMII/SDMMC/GPIO ·
10 DRAM DDR3/DDR3L · 11 SPI Flash · 12 TF Card · 13 VO MIPI-DSI ·
14 USB OTG / RTC · 15 Power-Discrete · 16 CORE-CONN-LED (J8001/J8002) ·
17 Revision History.
