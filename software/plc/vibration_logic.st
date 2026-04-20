(* PLC Logic - Structured Text (IEC 61131-3) 
   Vibration Shift Detection Logic 
   Threshold: 5% change vs baseline
   Persistence: 3 consecutive windows
*)

PROGRAM Vibration_Fault_Detection
VAR
    RMS_Window : REAL;       (* Calculated RMS for current window *)
    Baseline : REAL;         (* Established baseline *)
    Change : REAL;           (* Relative shift *)
    Counter : INT := 0;      (* Persistence counter *)
    Alarm : BOOL := FALSE;   (* Fault status *)
    THRESHOLD : REAL := 0.05;
END_VAR

(* Percentage Shift Calculation *)
IF Baseline > 0 THEN
    Change := (RMS_Window - Baseline) / Baseline;
END_IF;

(* Fault Persistence Logic *)
IF Change >= THRESHOLD THEN
    Counter := Counter + 1;
ELSE
    Counter := 0;
END_IF;

IF Counter >= 3 THEN
    Alarm := TRUE;
END_IF;
