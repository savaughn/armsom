# CM1 Board-to-Board Connectors — J8001 & J8002

Source: `ArmSoM-CM1-1V1_Sch.pdf` **sheet 16 (CORE-CONN-LED)**, rev V1.1.
These are the connectors on the **CM1 module** that mate to the carrier
(CM1-IO or custom). Extracted from word coordinates and verified against the
rendered page. The `[n]` after a net is the cross-reference to the SoC sheet
where that net originates.

Pin numbering: odd pins (1,3,5…) in the left column, even pins (2,4,6…) in the
right column — standard 2-row DIP order.

Unlabeled pins are shown as `— (unlabeled)`: on the schematic these tie to GND
or are NC. **Verify GND/NC pins against the PCB or CM1-IO mating schematic
before relying on them.**

---

## J8001 — `DIP_2D54_2X20P`, 40-pin (2×20, 2.54 mm)

Carrier-side this is the **40-pin user header**: UART2/3, I2C2, RMII0+RMII1
(both Ethernet MACs), USB OTG1, analog (ACODEC/SARADC), RUN LED, and power rails.

| Pin | Net (SoC default) | xref | Pin | Net (SoC default) | xref |
|----:|-------------------|:----:|----:|-------------------|:----:|
| 1 | — (unlabeled) | | 2 | **VCC_3V3** | |
| 3 | UART3_TX | [4] | 4 | **VCC_3V3** | |
| 5 | UART3_RX | [4] | 6 | **VCC_1V8** | |
| 7 | I2C2_SCL | [4,13,14] | 8 | I2C2_SDA | [4,13,14] |
| 9 | UART2_TX | [4] | 10 | UART2_RX/PWM0_CH3_IR_RX | [4] |
| 11 | RMII1_MDIO | [9] | 12 | RMII1_RXDV_CRS | [9] |
| 13 | RMII1_TXEN | [9] | 14 | RMII1_MDC | [9] |
| 15 | RMII1_TXD0 | [9] | 16 | RMII1_TXD1 | [9] |
| 17 | RMII1_RXD1 | [9] | 18 | RMII1_CLK | [9] |
| 19 | RMII0_RXDV_CRS | [9] | 20 | RMII1_RXD0 | [9] |
| 21 | RMII0_MDC | [9] | 22 | RMII0_MDIO | [9] |
| 23 | RMII0_TXD1 | [9] | 24 | RMII0_TXEN | [9] |
| 25 | RMII0_CLK | [9] | 26 | RMII0_TXD0 | [9] |
| 27 | RMII0_RXD0 | [9] | 28 | RMII0_RXD1 | [9] |
| 29 | ADC2/HOST_WAKE_BT_H | [7] | 30 | RUN_LED/ADC3 (via R9007 0Ω) | [7,16] |
| 31 | ACODEC_ADC_INP | [7] | 32 | ACODEC_ADC_INN | [7] |
| 33 | USB20_OTG1_DM | [7] | 34 | **VCC5V0_SYS** | |
| 35 | USB20_OTG1_DP | [7] | 36 | **VCC5V0_SYS** | |
| 37 | — (unlabeled) | | 38 | **VCC5V0_SYS** | |
| 39 | — (unlabeled, near GND) | | 40 | **VCC12V_DCIN** | |

Power on this connector: **VCC_3V3** (pins **2 / 4**, tied), **VCC_1V8** (pin 6),
**VCC5V0_SYS** (pins **34 / 36 / 38**, all three tied — schematic sheet 16
shows a common net, so the 5 V rail has three parallel pins for current
capacity), **VCC12V_DCIN** (pin 40, 12 V barrel/adapter in).

---

## J8002 — `DIP_2D54_2X22P`, 44-pin (2×22, 2.54 mm)

Carrier-side this is the **44-pin user header**: the full **FlexBUS1 / DSMC**
lane group (`FLEXBUS1_D0..D15` + `FLEXBUS1_CLK`), CAN0/CAN1, UART0 (console) +
UART4, I2C1, SAI1 audio, the DSM speaker-amp pair, the OTG0/OTG1 DRV controls,
WIFI_REG_ON, and the RTC backup-battery tap.

| Pin | Net (SoC default) | xref | Pin | Net (SoC default) | xref |
|----:|-------------------|:----:|----:|-------------------|:----:|
| 1 | DSMC_CLKP/**FLEXBUS1_D0** | [8] | 2 | DSMC_INT0/**FLEXBUS1_D1** | [8] |
| 3 | DSMC_DQS0/**FLEXBUS1_D2** | [8] | 4 | DSMC_D0/**FLEXBUS1_D3** | [8] |
| 5 | DSMC_D1/**FLEXBUS1_D4** | [8] | 6 | DSMC_D2/**FLEXBUS1_D5** | [8] |
| 7 | DSMC_D3/**FLEXBUS1_D6** | [8] | 8 | DSMC_D4/**FLEXBUS1_D7** | [8] |
| 9 | DSMC_D5/**FLEXBUS1_D8** | [8] | 10 | UART4_CTSN/**FLEXBUS1_D9** | [8] |
| 11 | CAN1_TX/**FLEXBUS1_D10** | [8] | 12 | CAN1_RX/**FLEXBUS1_D11** | [8] |
| 13 | DSMC_D6/**FLEXBUS1_D12** | [8] | 14 | DSMC_D7/**FLEXBUS1_D13** | [8] |
| 15 | DSMC_CSN0/**FLEXBUS1_D14** | [8] | 16 | DSMC_RDYN/**FLEXBUS1_D15** | [8] |
| 17 | DSMC_RESETN/**FLEXBUS1_CLK** | [8] | 18 | DSM_AUD_RN | [8] |
| 19 | DSM_AUD_RP | [8] | 20 | GPIO1_C3/MIPI_DPHY_DSI_TE | [8] |
| 21 | GPIO1_C4/USB20_OTG0_DRV_H | [8] | 22 | GPIO1_C5/WIFI_REG_ON_H | [8] |
| 23 | SPK_CTRL | [8] | 24 | RMII1_RSTn | [8] |
| 25 | USB20_OTG1_DRV_H | [8] | 26 | UART4_RTSN | [8] |
| 27 | UART4_RX | [8] | 28 | UART4_TX | [8] |
| 29 | PHONE_DET_L_1V8 | [4] | 30 | — (unlabeled) | |
| 31 | UART0_TX/JTAG_TCK_M1 | [4] | 32 | UART0_RX/JTAG_TMS_M1 | [4] |
| 33 | CAN0_RX | [4] | 34 | CAN0_TX | [4] |
| 35 | RMII0_RSTn | [4] | 36 | I2C1_SDA | [4] |
| 37 | **VBAT_RTC** | | 38 | I2C1_SCL | [4] |
| 39 | SAI1_SDO0 | [4] | 40 | SAI1_SDI | [4] |
| 41 | SAI1_LRCK | [4] | 42 | SAI1_SCLK | [4] |
| 43 | SAI1_MCLK | [4] | 44 | **GND** | |

**FlexBUS1 lane group** (the SoC's FlexBUS external-bus data/clock fabric):
D0–D15 on pins 1–16 (interleaved odd/even),
**FLEXBUS1_CLK on pin 17**. Each `FLEXBUS1_Dn` shares its pad with a DSMC,
CAN1, or UART4 function — selected by pinmux. **`flexbus1_data` is RECEIVE-ONLY
and these are NOT interchangeable with FlexBUS0 — read the ⚠ note below before
wiring any FlexBUS master (e.g. a QSPI NOR flash) to these pins.**

> **⚠ FB0 ≠ FB1 on these pads — `flexbus1_data` is INPUT-ONLY.** An earlier
> version of this note claimed FB0/FB1 are interchangeable and you can drive
> these pins as either controller. **That is wrong and cost a long hardware
> debug (2026-06-15).** Two facts from the SoC, both confirmed on hardware:
>
> 1. **`flexbus1_data` is receive-only.** RK3506 TRM Part 1 §37.1 (p.906):
>    *"The direction of flexbus0_data port is I/O … The direction of
>    flexbus1_data port is **Input**, flexbus1_data port can only be used for
>    receiving operation."* A FlexBUS **master** (SPI/FSPI, e.g. reading a QSPI
>    NOR) **cannot transmit** the command/address on `flexbus1_data` pins.
> 2. **The A-bank has NO `FLEXBUS0_*` alternate.** `GPIO1_A0..A7` mux to
>    `FLEXBUS1_D0..D7` *only*. The bidirectional `FLEXBUS0_D*` functions live on
>    the **B/C/D-bank** pads (below). So the J8002 pins silked `FLEXBUS1_D0..D3`
>    (pins 1–4, = `GPIO1_A0..A3`) **cannot** be re-muxed to FlexBUS0 output.
>
> ArmSoM's "functionally identical" was about CLK + the **slave-driven read**
> path (the slave drives `D0..D3`, the controller receives) — which agrees with
> the TRM, not with "drive A-bank pins as a FB0 master." Proof: a known-good
> Winbond W25Q128JV wired to `GPIO1_A0..A3` read JEDEC `00 00 00 00` for every
> `FLEXBUS_REMAP`/CS/clock combination; the same NOR works once rewired to the
> `FLEXBUS0_D*` C-bank pads.
>
> **To run a FlexBUS0 SPI/QSPI master (e.g. a NOR flash), the flash's data must
> be on bidirectional `FLEXBUS0_D*` pads** (`device_property … flexbus0-opmode =
> SPI`), with `FLEXBUS0_CLK` = `GPIO1_C1` (J8002.18) and a `FLEXBUS0_CSN_*`
> (e.g. `flexbus0_csn_m0` = `GPIO1_B0` = J8002.9). If the flash sits on a data
> group other than `FLEXBUS0_D0..D3`, program `FLEXBUS_REMAP` (0x010) to point
> the controller's lanes at it — the stock `flexbus-fspi` driver leaves it 0.
>
> **`FLEXBUS0_D*` pad map** (mux 3; bidirectional I/O):
>
> | FB0 data | SoC pad | J8002 | | FB0 data | SoC pad | J8002 |
> |---|---|---|---|---|---|---|
> | D0 | GPIO1_D3 | 28 | | D8  | GPIO1_C3 | 20 |
> | D1 | GPIO1_D2 | 27 | | D9  | GPIO1_C2 | —  |
> | D2 | GPIO1_D1 | 26 (backlight) | | D10 | GPIO1_B7 | 16 |
> | D3 | GPIO1_D0 | — | | D11 | GPIO1_B6 | 15 |
> | D4 | GPIO1_C7 | 24 | | D12 | GPIO1_B5 | 14 |
> | D5 | GPIO1_C6 | 23 | | D13 | GPIO1_B4 | 13 |
> | D6 | GPIO1_C5 | 22 | | D14 | GPIO1_B3 | 12 |
> | D7 | GPIO1_C4 | 21 | | D15 | GPIO1_B2 | 11 |
>
> Only the **B-bank** `FLEXBUS0_D10..D15` pins (J8002.11–16) double as
> `FLEXBUS1_D10..D15`; the A-bank does not.
>
> **Command-phase gotcha (RK3506 silicon, hardware-confirmed).** The FSPI
> command/address phase *always* exits on `flexbus0_d0` = `Dout[0]` =
> **GPIO1_D3 (J8002.28)**. `tx_data_remap` (low nibble of `FLEXBUS_REMAP`)
> relocates only the TX *data* phase, **not** the command — so a `0x14`
> (tx_remap=4) that tries to push the command onto the D4–D7 group is heard by
> nothing and JEDEC reads `00`. The flash's IO0/SI must therefore reach
> **GPIO1_D3** for the command; for quad, fan flash IO0 to **both** GPIO1_D3
> (command, `Dout[0]`) **and** its quad data lane.
>
> **Worked quad-NOR pin recipe on this module** (one validated combination):
> flash IO0 to both **GPIO1_D3** (J8002.28, command) and **GPIO1_C7** (J8002.24,
> quad data lane); quad read window `Din[7:4]` = GPIO1_C7/C6/C5/C4
> (J8002.24/23/22/21); `FLEXBUS0_CLK` = GPIO1_C1 (J8002.18); CS =
> `flexbus0_csn_m0` = GPIO1_B0 (J8002.9, mux 5); **`FLEXBUS_REMAP = 0x10`**
> (tx_remap=0 → command on `Dout[0]`=D3, rx_remap=1 → quad window
> `Din[7:4]`=C7..C4). The native `D0–D3` group is impossible on this module —
> GPIO1_D0 (`FLEXBUS0_D3`) is not pinned out on either connector.

> **Rev V1.1 change (sheet 17):** J8002 **pin 37 was reassigned to VBAT_RTC**
> (was something else in V1.0). It is the RTC backup-battery input. Also in
> V1.1: `WIFI_PWR_L` → `RTC_INT`; the LED net became `RUN_LED/ADC3`.

---

## Cross-reference sheet legend

The `[n]` tags point to the originating SoC sheet:

| Tag | CM1 sheet |
|----:|-----------|
| [4] | SOC-OSC/PLL/PMUIO (also carries UART/I2C/SAI/CAN/RMII-reset GPIO) |
| [7] | SOC-USB/ACODEC/SARADC (OTG1, analog in, ADC2/ADC3) |
| [8] | SOC pin-mux sheet for DSMC/FlexBUS1/DSM/GPIO1_C |
| [9] | SOC-RMII/SDMMC/GPIO |
| [13] | VO-MIPI-DSI |
| [14] | USB OTG0 / RTC |

## Notes for carrier / device-tree work

- **GPIO bank mapping**: the `GPIO1_Cx` and `FLEXBUS1_Dn` nets land in SoC
  GPIO bank 1. For Linux line offsets, GPIO1 offset = `gpio# − 32` (GPIO1 base
  = 32; GPIO1 chip @ `0xff870000`). Resolve exact offsets from the RK3506
  pinctrl DTSI, not from the net name.
- **Console UART** = UART0 on J8002.31 (TX) / J8002.32 (RX), shared with
  M1-core JTAG.
- **Display** is MIPI-DSI (sheet 13), *not* on these connectors except the
  optional **TE** strobe `GPIO1_C3/MIPI_DPHY_DSI_TE` on J8002.20.
- **Both RMII MACs** (RMII0 + RMII1) are fully pinned out on J8001; carriers
  that don't use Ethernet leave them free.
