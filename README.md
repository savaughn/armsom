# ArmSoM CM1 / CM1-IO — Claude Code plugin

Hardware reference skills for the **ArmSoM CM1** (Rockchip RK3506J) system-on-module
and its **CM1-IO** carrier board. The schematic data is pre-extracted into Markdown
so Claude can answer pin/power/peripheral questions without re-parsing the vendor
PDFs every time.

## Skills

| Skill | Covers |
|-------|--------|
| `armsom:cm1` | CM1 module: SoC overview, power tree, J8001/J8002 board-to-board connector pinouts, voltage domains, FSPI/SDMMC/MIPI-DSI/USB/RMII/audio/FlexBUS, boot strap |
| `armsom:cm1-io` | CM1-IO carrier: 40-pin GPIO/FlexBUS header (J4) with Linux gpio numbers, dual Ethernet (YT8522C), RK730 audio, CH334R USB hub, BL-M8733BU1 WiFi/BT, CAN/RS485, 12 V power tree |

Each skill carries its data under `reference/` and a reusable PyMuPDF schematic
extractor under `scripts/extract_schematic.py` (no poppler required).

## Install

```text
/plugin marketplace add https://github.com/savaughn/armsom.git
/plugin install armsom@armsom
```

Then the `armsom:cm1` and `armsom:cm1-io` skills activate automatically when a
task mentions the CM1, CM1-IO, RK3506, J8001/J8002, the 40-pin header, FlexBUS1,
etc.

## Source documents

These skills were extracted from the ArmSoM V1.1 schematics
(`ArmSoM-CM1-1V1_Sch.pdf`, `ArmSoM-CM1-IO-1V1_Sch.pdf`, rev 2025-06-10). The
documents themselves are not redistributed here; net names and pinouts are
transcribed for reference. Always confirm critical pin assignments against the
official schematic and the RK3506 TRM before committing a design change.

## Regenerating

```bash
python3 skills/cm1/scripts/extract_schematic.py <pdf> --text [PAGE]
python3 skills/cm1/scripts/extract_schematic.py <pdf> --render PAGE out.png
python3 skills/cm1/scripts/extract_schematic.py <pdf> --connectors PAGE --lx <x> --rx <x>
```
