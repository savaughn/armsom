# CM1-IO Onboard Peripherals

Source: `ArmSoM-CM1-IO-1V1_Sch.pdf` sheets 4–8, rev V1.1.

## Ethernet ×2 — 10/100 FEPHY (sheets 4, 5)

Two independent Fast-Ethernet PHYs convert the module's RMII MACs to copper:

| MAC | PHY | Ref | RJ45 | IO domain |
|-----|-----|-----|------|-----------|
| RMII0 | **Motorcomm YT8522C** | `U6601` | RJ45 (sheet 4) | VCCIO_RMII0 = 3.3 V |
| RMII1 | **Motorcomm YT8522C** | `U6701` | `J6700` LPJG0926HENL (integrated magnetics) | VCCIO_RMII1 (must match SoC VCCIO4) |

- PHY package `QFN32`. Reference clock: 25 MHz crystal `Y6700` (RMII1 side);
  RMII REF_CLK direction and XTAL/TXC source are strap-selectable.
- `PHYAD[1:0]` straps via LED0/LED1 pins, default PHY address = 1 (`2'b01`).
- WOL/LED0, MII/RMII, and UTP/Fiber selects are resistor straps (see sheet
  notes). MII/RMII pulled high = RMII mode (default).
- **RMII1 is optional / shared** with SAI2 / UART5 on the SoC — fitting the
  second PHY trades those functions.
- Nets `RMII0_*` route to core-connector sheet 2 `[4]`; `RMII1_*` to `[5]`.
  Each line has 22 Ω series + the PHY's own termination.

## Audio — RK730 codec + class-D amp (sheet 6)

- **Codec**: Rockchip **RK730** (`U7000`, QFN28). I²C control on a dedicated
  bus, 7-bit address **0x17** (CE=H, default) or **0x16** (CE=L). I²S on the
  module's **SAI1** (`SAI1_MCLK/SCLK/LRCK/SDI/SDO0`).
- **Speaker amp**: **TCS7191A** (`U7300`, MSOP8) mono class-D, gain
  = Rf/(Ri+6k) = 576k/(75k+6k) ≈ **7.1**, high-pass Fc ≈ 196 Hz, enabled by
  `SPK_CTRL`. Output `SPKP_OUT/SPKN_OUT` to the speaker connector.
- **Mic**: differential `MICIN_1P/1N`, `MICIN_2P/2N` with `CODEC_MIC_BIAS`.
- **Headphone**: `LOUT1/ROUT1` (and `LOUT2/ROUT2`) to phone jack `J7`
  (`PJ35106SY`), with `PHONE_DET_L_1V8` detect.
- **External audio header** `J8005` (`DIP_2D54_2X6P`) exposes speaker / mic /
  line nets. The CAN/RS485 connector nets (`CAN_H/L_CON`, `RS485_A/B_CON`)
  also pass through this sheet to the transceivers on sheet 8.
- Rails: VCC_PA (amp), VCC_3V3, VCC_1V8.

## USB hub + WiFi/BT (sheet 7)

- **USB 2.0 hub**: **CH334R** (`U9402`) — fans the module's `USB20_OTG1`
  (`HUB20_*`) into multiple downstream ports.
- **Type-A dual receptacle** `J8` (`USB2_TYPEA_DUAL_DIP`) on two downstream
  ports, with `ESD5341N` per line and per-port power.
- **Port power switch**: **SGM2590D / TCS9163** (`U2501`), current limit
  `Ilim = (6612/RILIM)·0.982 A` — size RILIM to the load.
- **WiFi/BT module**: **BL-M8733BU1** (`U9403`) on a hub port (`USB_DP/DM`),
  with PCM audio to BT, `CHIP_EN`, `WL_DIS`/`BT_DIS`, `HOST_WAKE_*`, antenna
  connectors `J5`/`J6` (`ANT_RF4`), 12 MHz ref `Y6000`. Powered from
  `VBAT_WL`; enabled via the module's `WIFI_REG_ON` (`GPIO1_C5`).

## CAN0 (sheet 8)

- **TCAN1044V-Q1** (`U9400`, SOP8). PIN3=5 V, PIN5=VIO, PIN8=STB.
  (Alternate `TCS9163`/`TCAN332G`: PIN3=3.3 V, PIN5/8=NC.)
- SoC side `CAN0_TX/CAN0_RX`; bus side `CANH/CANL` → `CAN_H_CON/CAN_L_CON`.
  VIO from `VCC_CAN`. Note CM1 also brings out **CAN1** on the FlexBUS group
  (`CAN1_TX/RX = FLEXBUS1_D10/D11`).

## RS485 (sheet 8)

- **SIT3485E** (`U9301`, SOP8; alt `TPT485N`/`UM13088`). Direction control
  `RS485_DE` (`RE/DE`: 0 = RX, 1 = TX). Bus `RS485_1A/1B` → `RS485_A/B_CON`.
- **120 Ω termination** (`R9325`/`R9410`, NC by default) — fit only on the two
  physical ends of the bus.
- A `9.1k/910Ω` bias divider (`R65`/`R66`) idles the bus.

## Debug / misc (sheet 8)

UART3 (`UART3_TX/RX`) is broken out as a debug port alongside the 40-pin
header. `ADC2/HOST_WAKE_BT_H` doubles as a 1.8 V ADC input.
