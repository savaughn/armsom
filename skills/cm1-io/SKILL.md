---
name: cm1-io
description: >-
  ArmSoM CM1-IO carrier board hardware reference (the baseboard the ArmSoM CM1 /
  RK3506J module plugs into). Pre-extracted schematic data so you never have to
  re-parse the ArmSoM CM1-IO PDF: the 40-pin GPIO/FlexBUS header (J4) pinout with
  Linux gpio numbers and RM_IO indices, the J8001/J8002 core-connector mating map,
  and every onboard peripheral — dual 10/100 Ethernet (YT8522C PHYs + RJ45), RK730
  audio codec + speaker amp + phone jack, USB hub (CH334R) + Type-A ports, WiFi/BT
  module (BL-M8733BU1), CAN (TCAN1044V) and RS485 (SIT3485E) transceivers, and the
  12 V DC-in power tree. Use whenever a task touches the CM1-IO / carrier: header
  pin assignment, "which gpio is J4 pin N", FlexBUS1 lane breakout, device-tree
  pinmux, Ethernet/USB/audio/CAN/RS485 wiring, or power. Trigger on "CM1-IO",
  "carrier", "baseboard", "40-pin header", "J4", "YT8522C", "RK730", "CH334R",
  "BL-M8733BU1", "FLEXBUS1", or any question answerable from the CM1-IO schematic.
  The module-side reference is the sibling `armsom:cm1` skill.
---

# ArmSoM CM1-IO Carrier Reference

The **CM1-IO** (schematic title "ArmSoM-FORGE1-IO", rev V1.1, 2025-06-10) is the
carrier board the **CM1** RK3506J module mounts on via the **J8001 (40-pin)** and
**J8002 (44-pin)** board-to-board connectors. This skill holds the data extracted
from `ArmSoM-CM1-IO-1V1_Sch.pdf` (9 sheets) so carrier questions are answered
without re-rendering the PDF. For the module itself (SoC, power tree, core
connector net map) use the sibling **`armsom:cm1`** skill.

## How to use this skill

1. **40-pin user header (J4)** — gpio#, RM_IO#, FlexBUS1 lane per pin →
   [reference/cm1io-40pin-header.md](reference/cm1io-40pin-header.md). Most
   common lookup. The authoritative vendor pinout image is bundled at
   [reference/assets/cm1io-40pin-header.png](reference/assets/cm1io-40pin-header.png).
2. **Onboard peripherals** (Ethernet, audio, USB hub, WiFi/BT, CAN, RS485) →
   [reference/cm1io-peripherals.md](reference/cm1io-peripherals.md).
3. **Other connectors** (DC jack, phone jack, USB Type-A, audio header, RJ45,
   antennas, core connector) → [reference/cm1io-connectors.md](reference/cm1io-connectors.md).
4. **Power tree** (12 V in → rails) → [reference/cm1io-power.md](reference/cm1io-power.md).
5. **Board overview / sheet index** → [reference/cm1io-overview.md](reference/cm1io-overview.md).

Cite the source sheet when you answer (e.g. "CM1-IO sch sheet 8, GPIO-40PIN
Header"). If a fact is not here, say so before rendering the PDF.

## Ground rules

- **Header nets are SoC default pad functions** (often a `/`-mux label). Actual
  behavior depends on the RK3506 device-tree pinmux — the silk/net name is not
  proof of how a pin is driven.
- The **GPIO Number** in the J4 table is the **Linux global gpio number**
  (`gpiochipN` line = number − bank_base; GPIO0 base 0, GPIO1 base 32,
  GPIO4 base 128). It cross-checks against bank math, but confirm against the
  RK3506 pinctrl DTSI before committing a pinmux.
- The carrier re-exposes the module's J8001/J8002 nets unchanged; net names
  match the `armsom:cm1` connector tables one-for-one.
- This skill documents the board as designed and encodes no product-specific
  usage or device-tree choices.

## Regenerating / extending

Same PyMuPDF extractor as the module skill (no poppler):

```bash
python3 scripts/extract_schematic.py ArmSoM-CM1-IO-1V1_Sch.pdf --text [PAGE]
python3 scripts/extract_schematic.py ArmSoM-CM1-IO-1V1_Sch.pdf --render PAGE out.png
python3 scripts/extract_schematic.py ArmSoM-CM1-IO-1V1_Sch.pdf --connectors 8 --lx 593 --rx 626 --xband 430 820
```

## Source document

| File | What it is | Rev |
|------|------------|-----|
| `ArmSoM-CM1-IO-1V1_Sch.pdf` | CM1-IO carrier schematic, 9 sheets | V1.1 (2025-06-10) |

Sheet index: 1 Block Diagram · 2 CORE-CONN (J8001/J8002 mating) ·
3 Power-DC IN · 4 Ethernet FEPHY RMII0 · 5 Ethernet FEPHY RMII1 ·
6 Audio-Codec (RK730 + amp + CAN/RS485 jacks) · 7 USB-HUB / WiFi-BT ·
8 GPIO-40PIN Header + CAN0 + RS485 · 9 Revision History.
