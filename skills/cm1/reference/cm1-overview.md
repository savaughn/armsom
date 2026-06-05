# CM1 Module Overview

Source: `ArmSoM-CM1-1V1_Sch.pdf` **sheet 1 (Block Diagram)**, rev V1.1
(2025-06-10), designer "Park". The module is also referred to in the block
diagram as "ArmSoM-FORGE1".

## SoC: Rockchip RK3506J

- **Part fitted**: **RK3506J** — the industrial-grade variant (extended
  temperature / higher thermal tolerance). The schematic *symbol* is drawn as
  the generic die family **"RK3506B"** (e.g. `U1000x RK3506B`); the populated
  module SoC is the RK3506J. Treat "RK3506B" on the sheets as the base-family
  silk, not the assembled part.
- **CPU**: triple-core ARM Cortex-A7 + single Cortex-M0.
- **Package**: `BGA333_13R3X11R3X1R25`.
- **Memory**: on-module DDR3/DDR3L, 1×16-bit (sheets 5, 10). Fitted DDR3L
  @ 1.36 V.
- **Boot flash**: on-module SPI NOR via FSPI (sheet 11).

## SoC peripheral inventory (from block diagram)

- **Display/VOP**: RGB888 / BT1120 / BT656 parallel **or** MIPI-DPHY DSI
  (1× 2-lane). The fitted panel interface on this module is MIPI-DSI.
- **FLEXBUS0~1** + **DSMC** (8/16-bit slave) — the high-speed external bus
  fabric; the FlexBUS1 lane group is exposed on J8002.
- **FSPI** (SPI NOR/NAND), **SDMMC** (4-bit), **SPI0~1**, **SPI2 (slave)**.
- **UART0–5** (UART0 + JTAG), **I2C0~2**, **CAN0~1**.
- **RMII0~1** (dual Ethernet MAC, no on-module PHY), optional FEPHY.
- **USB**: OTG0, OTG1, plus USB2.0 host ports (carrier).
- **Audio**: SAI0~3 (I2S), SPDIF TX/RX, ACODEC (ADC + HP/MIC), PDM 4RX,
  AUDDSM L/R class-D, audio loopback.
- **PWM0 (CH0–3)**, **PWM1 (CH0–7)**, **SARADC0~3**, **TOUCH KEY ×8**.
- **RM_IO0~31** — the RK3506 flexible IO mux crossbar (lets many functions
  land on `GPIO1_*` etc.).

## Physical interface to the carrier

Two board-to-board connectors carry everything off-module:

- **J8001** — 40-pin (`DIP_2D54_2X20P`): UART2/3, I2C2, dual RMII, USB OTG1,
  analog in, RUN LED, power rails (3V3/1V8/5V/12V).
- **J8002** — 44-pin (`DIP_2D54_2X22P`): FlexBUS1 lane group, CAN0/1, UART0
  console + UART4, I2C1, SAI1 audio, DSM speaker, OTG drive controls,
  WIFI_REG_ON, RTC battery.

Full pinouts: [cm1-connectors.md](cm1-connectors.md).

## Revision history (sheet 17)

| Ver | Date | Change |
|-----|------|--------|
| V1.0 | 2024-12-25 | First release |
| **V1.1** | 2025-06-10 | RTC: **J8002.37 → VBAT_RTC**; add D2200 & R2226; `WIFI_PWR_L` → `RTC_INT`; LED signal `ADC3` → `RUN_LED/ADC3` |

The extracted reference in this skill reflects **V1.1**.
