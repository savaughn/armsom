# CM1-IO Connectors & Headers

Source: `ArmSoM-CM1-IO-1V1_Sch.pdf`, rev V1.1. Reference designators as drawn.

## Core connectors (module mating) — sheet 2 "CORE-CONN"

`J8001` (40-pin) and `J8002` (44-pin) mate to the CM1 module. The carrier-side
net names are **identical** to the module side — for the full pin↔net tables
use the **`armsom:cm1`** skill (`reference/cm1-connectors.md`). On the CM1-IO
schematic the cross-reference `[n]` after each core-connector net points to the
carrier sheet that consumes it:

| Tag | CM1-IO sheet |
|----:|--------------|
| [2] | CORE-CONN (this sheet) |
| [4] | Ethernet FEPHY RMII0 |
| [5] | Ethernet FEPHY RMII1 |
| [6] | Audio-Codec (+ CAN/RS485 jacks) |
| [7] | USB-HUB / WiFi-BT |
| [8] | GPIO-40PIN Header + CAN0 + RS485 |

Power/strap nets crossing the core connector: `VCC12V_DCIN`, `VCC5V0_SYS`,
`VCC_3V3`, `VCC_1V8`, `VBAT_RTC`.

## User-facing connectors

| Ref | Type / part | Sheet | Purpose |
|-----|-------------|------:|---------|
| **J4** | 40-pin 2×20 `DIP_2D54_2X20P` | 8 | GPIO / FlexBUS / UART0 console / SARADC — see [cm1io-40pin-header.md](cm1io-40pin-header.md) |
| **J1** | `DC-528-2.0` barrel jack | 3 | **12 V DC input** (VCC12V_DCIN) |
| **J7** | `PJ35106SY` phone jack | 6 | Headphone out + `PHONE_DET_L` |
| **J8005** | 2×6 `DIP_2D54_2X6P` | 6 | External audio header (speaker / mic / line) |
| **J8** | `USB2_TYPEA_DUAL_DIP` | 7 | Dual USB 2.0 Type-A (downstream of CH334R hub) |
| RJ45 (RMII0) | sheet-4 magjack | 4 | Ethernet port 0 (YT8522C) |
| **J6700** | `LPJG0926HENL` RJ45 + magnetics | 5 | Ethernet port 1 (YT8522C) |
| **J5 / J6** | `818000500` `ANT_RF4` | 7 | WiFi / BT antenna connectors |

Audio/CAN/RS485 field wiring (`SPKP/N_OUT`, `MICIN_*`, `CAN_H/L_CON`,
`RS485_A/B_CON`) terminates on the audio header / pluggable terminals fed from
sheets 6 and 8.

## Power & USB Type-C

The CM1-IO takes **12 V at J1**; the module's USB-C (OTG0) lives on the CM1
module itself (see `armsom:cm1`). USB host ports on the carrier are OTG1 routed
through the CH334R hub to `J8`.
