# CM1 SoC Peripherals, Voltage Domains & Boot Strap

Source: `ArmSoM-CM1-1V1_Sch.pdf` sheets 4, 6, 7, 8, 9, 11, 12, 13, 14, rev V1.1.
The SoC is the **RK3506J** (industrial variant) in a `BGA333_13R3X11R3X1R25`
package. The schematic symbol is labelled with the base family "RK3506B"; the
fitted part is the RK3506J.

## Voltage domains (VCCIO)

| Domain | Sheet | Operating voltage | Signals |
|--------|------:|-------------------|---------|
| PMUIO_VCC3V3 | 4 | 3.3 V | PMU / OSC / reset / I2C2 / UART0 / SAI1 / boot |
| VCCIO2 (FLASH) | 6 | **1.8 V / 3.3 V** | FSPI (`FSPI_CSN/CLK/D0..D3`), GPIO2_A0–A5 |
| VCCIO4 | 9 | **1.8 V / 3.3 V** | SDMMC, RMII1, GPIO3 |
| OSC/PLL | 4 | 1.8 V | 24 MHz crystal, analog |
| VCC_DDR | 5,10 | 1.36 V (DDR3L) | DDR3/DDR3L 1×16-bit |

The flash/SDMMC IO domains are **selectable 1.8/3.3 V** — match the level to
the fitted flash/card. Default fitted flash is 3.3 V (sheet 11).

## Clocks / reset (sheet 4)

- **24 MHz crystal** Y1100 on `OSC_XIN`/`OSC_XOUT` (18 pF loading caps,
  1 MΩ bias, 22 Ω series). OSC/PLL operates at 1.8 V.
- **RK801-1 PMIC** control path drives nPOR / reset.
- I2C2 (`I2C2_SCL`/`SDA`) is the PMU/system I2C — shared with the panel
  (sheet 13), RTC (sheet 14), and exposed on J8001.7/8.

## FSPI flash (sheets 6, 11)

On-module **SPI NOR flash** `U4300` (`WSON8`): `FSPI_CLK/CSN/D0(DI)/D1(DO)/
D2(WP)/D3(HOLD)`, VCCIO_FLASH domain. Pads: `FSPI_CSN=GPIO2_A0`,
`CLK=GPIO2_A1`, `D0=GPIO2_A2`, `D1=GPIO2_A3`, `D2=GPIO2_A4`, `D3=GPIO2_A5`
(all bank GPIO2_A). 10 K pulls on CS/HOLD. Refer to AVL for the exact part.

## SDMMC / TF card (sheets 9, 12)

`SDMMC_CLK/CMD/D0..D3` (GPIO3_A0–A5, VCCIO4). TF socket `J16` (push-push), with
**22 Ω series + ESD5341N** on each line, **SDMMC_DET_L** card-detect (to
sheet 4). SD lines also mux with JTAG_M0 / SAI2 / RMII1 on GPIO3.

## MIPI-DSI display (sheet 13)

2-lane MIPI-DPHY DSI panel interface on FPC `J25` (15-pin, 1.0 mm):
`MIPI_DPHY_DSI_TX_D0±`, `D1±`, `CLK±`, plus `I2C2` for touch, `TP_RST_L`,
`TP_INT_L`, `LCD_PWREN_H`, and `VCC3V3_LCD` (switched by Q5000/Q5001). The
optional **TE** strobe is `GPIO1_C3/MIPI_DPHY_DSI_TE`, exposed on J8002.20.

A parallel **RGB888 / BT1120 / BT656 LCDC (VOP)** path also exists on the SoC
(sheet 8) sharing the same pads via pinmux — it is an alternative to MIPI-DSI,
not additive. Sheet 8 is a large pad/function mux matrix; consult it directly
if doing parallel-RGB routing.

## USB (sheets 7, 14)

- **USB2.0 OTG0** — `USB20_OTG0_DP/DM`, `VBUSDET`, `ID`; wired to a **Type-C**
  receptacle `J2500` (sheet 14) with CC resistors. Drive enable
  `GPIO1_C4/USB20_OTG0_DRV_H`.
- **USB2.0 OTG1** — `USB20_OTG1_DP/DM` brought to J8001.35/33; drive enable
  `USB20_OTG1_DRV_H` (J8002.25).

## Ethernet (sheets 9, 16)

**Two RMII MACs**: RMII0 and RMII1, both fully pinned to J8001 (see connector
table). `RMII0_RSTn` on J8002.35, `RMII1_RSTn` on J8002.24. No on-module PHY —
the carrier provides PHY + magnetics.

## Audio (sheets 4, 7, 16)

- **SAI1** (I2S): `SAI1_MCLK/SCLK/LRCK/SDI/SDO0` on J8002.39–43.
- **ACODEC ADC** analog mic in: `ACODEC_ADC_INP/INN` (J8001.31/32), with
  `ADC_AVDD1V6`, `ADC_VCM` references (sheet 7).
- **DSM** class-D speaker pair `DSM_AUD_RP/RN` (J8002.18/19), `SPK_CTRL`
  (J8002.23), `VCC_PA`.

## SARADC / boot strap (sheet 7)

`SARADC_IN0_BOOT` selects the boot device via a resistor divider into ADC
channel 0 (Rup/Rdown pair → one of 10 ADC levels). Boot-order options include:

- `FSPI → SDMMC(eMMC/SD) → USB/SPI2APB`
- `SDMMC(eMMC/SD) → USB/SPI2APB`
- `FSPI → USB/SPI2APB`
- `USB (Maskrom mode) / SPI2APB`
- `SPI2APB`

`SARADC_IN1_RECOVER/KEY` is the recovery/key input. `ADC2/HOST_WAKE_BT_H`
(J8001.29) and `RUN_LED/ADC3` (J8001.30) are the other SARADC channels.
The exact resistor-to-level mapping is the RK3506 BOOT TABLE on sheet 7; read
it from the PDF if you need to change the strap.

## Other GPIO of note

- `GPIO1_C5/WIFI_REG_ON_H` (J8002.22) — WiFi module power/enable.
- `PHONE_DET_L_1V8` (J8002.29) — headphone-jack detect (1.8 V).
- `UART2_RX/PWM0_CH3_IR_RX` (J8001.10) — doubles as PWM/IR.
- `RTC_INT` (sheet 14, ex-`WIFI_PWR_L` in V1.0) — RTC interrupt.
