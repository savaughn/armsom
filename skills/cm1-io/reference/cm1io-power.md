# CM1-IO Power Tree

Source: `ArmSoM-CM1-IO-1V1_Sch.pdf` **sheet 3 (Power-DC IN)**, rev V1.1.

## Input

- **J1** `DC-528-2.0` barrel jack → **VCC12V_DCIN** (12 V / 2 A typical).
- Input protection: fuse **F2000** (`JK-SMD0805-300L`, polyfuse), reverse/clamp
  **SS34** Schottky (`D2000`) and **SMAJ15CA** TVS (`D63`), bulk 22 µF caps.
- Valid input range for the main buck: **4.5 V < VIN < 18 V** ("> 8 V → ON").

## Regulation

| Rail | From | Device | Notes |
|------|------|--------|-------|
| **VCC12V_SYS** | VCC12V_DCIN | direct (fused/protected) | 12 V distribution |
| **VCC5V0_SYS** | VCC12V_DCIN | **TMI3252SH / ETA8120** buck (`U2207`, SOT23-6) | 5 V system rail; FB = 0.6 V, VEN min 1.5 V |

- The buck uses an external inductor `L2204` (`MWSA0503S-4R7`) and the usual
  BOOT/EN/FB network. EN threshold ≈ 1.5 V; turns on above ~8 V input.
- **VCC5V0_SYS** is then handed to the **CM1 module** (via the core connector),
  which generates the SoC rails (VCC_3V3, VCC_1V8, VCC_DDR, VDD_CPU, VDD_0V9) —
  see the `armsom:cm1` power reference. The carrier itself mostly consumes
  VCC5V0_SYS, VCC_3V3, VCC_1V8 supplied back across the connector.

## Downstream switched rails (other sheets)

- **VCC5V0_USB20_OTG1** — USB port power via SGM2590D/TCS9163 load switch
  (`U2501`), current-limited (sheet 7).
- **VBAT_WL** — WiFi/BT module supply (sheet 7).
- **VCC_PA** — speaker-amp supply (sheet 6).
- **VCC_CAN** — CAN transceiver VIO (sheet 8).
- **VCCIO_RMII0 / VCCIO_RMII1** — Ethernet PHY IO (3.3 V; RMII1 must match SoC
  VCCIO4), with separate analog `VCCA3V3_RMII*` (sheets 4, 5).
- **VBAT_RTC** — RTC backup, passed from the module (J8002.37).

## Notes

- The board is **12 V-in only** at J1; do not back-feed 5 V into VCC5V0_SYS
  expecting the module to run without the 12 V→5 V stage unless that rail is
  supplied directly.
- Keep the 5 V buck input/output caps close to `U2207` per the layout notes.
