# CM1-IO Carrier Overview

Source: `ArmSoM-CM1-IO-1V1_Sch.pdf` **sheet 1 (Block Diagram)**, rev V1.1
(2025-06-10), title "ArmSoM-FORGE1-IO", designer "Park".

The CM1-IO is the baseboard for the **CM1 (RK3506J)** module. It supplies power,
breaks the SoC's IO out to standard connectors, and adds the physical-layer
parts the module omits (Ethernet PHYs, USB hub, audio codec/amp, WiFi/BT,
CAN/RS485 transceivers).

## What the carrier adds

| Function | Parts | Sheet |
|----------|-------|------:|
| 12 V → 5 V power | DC jack J1, TMI3252SH/ETA8120 buck | 3 |
| Ethernet ×2 (10/100) | 2× YT8522C PHY + RJ45 | 4, 5 |
| Audio | RK730 codec, TCS7191A amp, phone jack | 6 |
| USB hub + ports | CH334R hub, dual Type-A J8 | 7 |
| WiFi / Bluetooth | BL-M8733BU1 (USB) | 7 |
| CAN0 | TCAN1044V-Q1 | 8 |
| RS485 | SIT3485E | 8 |
| 40-pin GPIO/FlexBUS header | J4 | 8 |

## Module ↔ carrier interface

Two board-to-board connectors carry every signal between module and carrier:

- **J8001** (40-pin) — UART2/3, I2C2, dual RMII, USB OTG1, analog, power.
- **J8002** (44-pin) — FlexBUS1 lane group, CAN0/1, UART0 console + UART4, I2C1,
  SAI1 audio, DSM speaker, OTG drive, WIFI_REG_ON, RTC battery.

Net names are identical on both sides; the authoritative pin↔net tables live in
the **`armsom:cm1`** skill. This skill adds the carrier's onboard circuits and
the **gpio numbers** for the J4 user header.

## Sheet index

1. Block Diagram (ArmSoM-FORGE1-IO)
2. CORE-CONN — J8001/J8002 mating, net cross-reference
3. Power-DC IN — 12 V jack, 5 V buck
4. Ethernet FEPHY RMII0 — YT8522C `U6601`
5. Ethernet FEPHY RMII1 — YT8522C `U6701` (+ RJ45 `J6700`)
6. Audio-Codec — RK730 `U7000`, amp TCS7191A `U7300`, phone jack `J7`,
   audio header `J8005`
7. USB-HUB / WiFi-BT — CH334R `U9402`, BL-M8733BU1 `U9403`, USB-A `J8`
8. GPIO-40PIN Header `J4` + CAN0 `U9400` + RS485 `U9301`
9. Revision History

## Revision

Sheet 9 of the PDF carries the V1.1 revision note (2025-06-10). Both the CM1
module and CM1-IO carrier are at **V1.1**.
