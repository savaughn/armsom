# CM1-IO 40-pin GPIO / FlexBUS Header (J4)

Source: `ArmSoM-CM1-IO-1V1_Sch.pdf` **sheet 8 (GPIO-40PIN Header)**, ref `J4`
(`DIP_2D54_2X20P`), cross-checked against the vendor pinout table bundled at
[assets/cm1io-40pin-header.png](assets/cm1io-40pin-header.png) — **that image is
the authoritative per-pin source; consult it for every mux alternate.**

Every signal pin carries a **22 Ω series resistor** between the SoC pad and the
header (ESD/edge-rate). Most pins also have `PSM712`/`SM712` ESD protection.

## GPIO numbering

The header's **GPIO Number = Linux global gpio number**. Bank bases:
`GPIO0 = 0`, `GPIO1 = 32`, `GPIO2 = 64`, `GPIO3 = 96`, `GPIO4 = 128`.
Line within a chip = `gpio# − base`; each bank has 32 lines (A0–7=0–7,
B0–7=8–15, C0–7=16–23, D0–7=24–31). Examples: `gpio32 = GPIO1_A0`,
`gpio48 = GPIO1_C0`, `gpio138 = GPIO4_B2`, `gpio22 = GPIO0_C6`.

## Pinout

Odd pins (left, 1–39), even pins (right, 2–40). `gpio#` and pad are reliable;
the **Function** column lists the SoC default / primary mux — see the bundled
image for the complete alternate list per pin.

| Pin | gpio# | Pad | Function (primary) | Pin | gpio# | Pad | Function (primary) |
|----:|------:|-----|--------------------|----:|------:|-----|--------------------|
| 1 | — | — | **+3.3V** | 2 | — | — | **+5.0V** |
| 3 | 4 | GPIO0_A4 | RM_IO4 / SAI0_SDI0 | 4 | — | — | **+5.0V** |
| 5 | 5 | GPIO0_A5 | RM_IO5 / SAI0_SDI1 | 6 | — | — | **GND** |
| 7 | 59 | GPIO1_D3 | DSMC_RDYN / UART5_RX_M1 (RM_IO31) | 8 | 22 | GPIO0_C6 | **UART0_TX** (console) / JTAG_TCK_M1 (RM_IO22) |
| 9 | — | — | **GND** | 10 | 23 | GPIO0_C7 | **UART0_RX** (console) / JTAG_TMS_M1 (RM_IO23) |
| 11 | 58 | GPIO1_D2 | DSMC_CSN0 / UART5_TX_M1 (RM_IO30) | 12 | 57 | GPIO1_D1 | DSMC_SLV_D7 / UART5_RTSN_M1 / DSM_AUD_LP_M0 (RM_IO29) |
| 13 | 52 | GPIO1_C4 | DSMC_SLV_D2 / FLEXBUS0_D7 / VO_LCDC_D7 | 14 | 53 | GPIO1_C5 | DSMC_SLV_D3 / FLEXBUS0_D6 |
| 15 | 51 | GPIO1_C3 | DSMC_SLV_D1 / SAI2_SDO_M1 (RM_IO28) | 16 | 50 | GPIO1_C2 | DSMC_SLV_D0 / SAI2_SDI_M1 (RM_IO27) |
| 17 | — | — | **+3.3V** | 18 | 49 | GPIO1_C1 | DSMC_SLV_DQS0 / SAI2_MCLK_M1 / DSM_AUD_RN_M0 |
| 19 | 48 | GPIO1_C0 | DSMC_SLV_CLK / DSMC_INT1 / FLEXBUS1_CLK | 20 | 138 | GPIO4_B2 | **SARADC_IN2** (ADC2, 1.8 V) |
| 21 | 46 | GPIO1_B6 | FLEXBUS0_CSN_M3 / DSMC_CSN0 | 22 | 47 | GPIO1_B7 | FLEXBUS1_CSN_M3 |
| 23 | 44 | GPIO1_B4 | FLEXBUS0_CSN_M2 / DSMC_D6 | 24 | 45 | GPIO1_B5 | FLEXBUS1_CSN_M2 |
| 25 | — | — | **GND** | 26 | 43 | GPIO1_B3 | SAI2_LRCK_M1 / FLEXBUS1_CSN_M1 (RM_IO26) |
| 27 | 41 | GPIO1_B1 | UART5_CTSN_M1 (RM_IO24) | 28 | 42 | GPIO1_B2 | SAI2_SCLK_M1 / FLEXBUS0_CSN_M1 (RM_IO25) |
| 29 | 40 | GPIO1_B0 | DSMC_D5 / VO_LCDC_D19 | 30 | — | — | **GND** |
| 31 | 38 | GPIO1_A6 | DSMC_D3 / VO_LCDC_D21 | 32 | 39 | GPIO1_A7 | DSMC_D4 / VO_LCDC_D20 |
| 33 | 37 | GPIO1_A5 | DSMC_D2 / VO_LCDC_CLK | 34 | 36 | GPIO1_A4 | DSMC_D1 / VO_LCDC_D22 |
| 35 | 35 | GPIO1_A3 | DSMC_D0 | 36 | 34 | GPIO1_A2 | DSMC_DQS0 |
| 37 | 33 | GPIO1_A1 | DSMC_INT0 / DSMC_CLKN | 38 | — | GPIO1_A1 | DSMC_INT0 / VO_LCDC_HSYNC — *verify gpio# in image* |
| 39 | 32 | GPIO1_A0 | DSMC_CLKP / VO_LCDC_DEN | 40 | — | GPIO1_A0 | VO_LCDC_DEN — *verify gpio# in image* |

> **Accuracy note.** Pin numbers, power/GND pins, gpio numbers and pads above
> are read directly and cross-validated by bank math. Each FlexBUS-capable pin
> exposes several mux alternates (FLEXBUS0_*, FLEXBUS1_*, DSMC_*, VO_LCDC_*,
> SAI2_*, UART5_*M1) — the **FLEXBUS1_Dn lane numbers do not follow a simple
> A0→D0 sequence** across this header, so the full alternate list per pin is
> intentionally left to the bundled vendor image and the RK3506 TRM rather than
> transcribed here. The two bottom-right cells (pins 38, 40) are marked for
> verification against the image.

## Highlights for bring-up

- **Linux console**: UART0 on **pin 8 (TX, gpio22)** / **pin 10 (RX, gpio23)**.
  1.5 Mbaud 8N1, 3.3 V logic.
- **Power**: +3.3 V on pins 1, 17; +5.0 V on pins 2, 4; GND on 6, 9, 25, 30
  (plus header shield).
- **SARADC_IN2 / ADC2** on **pin 20 (gpio138)** — 1.8 V max input.
- Pins 7–40 (excl. power/GND) break out the **GPIO1 bank** — the same
  DSMC / FlexBUS1 fabric that appears on the module's J8002. The corresponding
  module-side net names (`DSMC_Dx/FLEXBUS1_Dy`) are in the `armsom:cm1` skill's
  connector table; this header adds the **gpio numbers** needed for pinmux.
- On sheet 8 these pins also feed the onboard **CAN0** (TCAN1044V-Q1, `U9400`)
  and **RS485** (SIT3485E, `U9301`) transceivers — see
  [cm1io-peripherals.md](cm1io-peripherals.md).
