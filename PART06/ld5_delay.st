PROGRAM conveyor
  VAR
    RAW_A    AT %IX0.3 : BOOL;     (* 센서 A 원래 값  GPIO17 · 물리 11번 *)
    RAW_B    AT %IX0.4 : BOOL;     (* 센서 B 원래 값  GPIO27 · 물리 13번 *)
    SENSOR_A AT %QX1.3 : BOOL;     (* 센서 A  1 = 감지 (렁 0 에서 뒤집음) *)
    SENSOR_B AT %QX1.4 : BOOL;     (* 센서 B  1 = 감지 *)
    MOVE_RIGHT AT %QX0.2 : BOOL;  (* 정방향  GPIO23 · 물리 16번 = IN1 *)
    MOVE_LEFT  AT %QX0.3 : BOOL;  (* 역방향  GPIO24 · 물리 18번 = IN2 *)
    A_DONE : BOOL;                 (* A 에서 3 초 기다림 끝 *)
    B_DONE : BOOL;
    TA : TON;                      (* On-Delay 타이머 *)
    TB : TON;
  END_VAR
  (* 0 : 센서 뒤집기 — D0 는 감지 = 0 이므로 NOT 으로 1 = 감지 *)
  SENSOR_A := NOT RAW_A;
  SENSOR_B := NOT RAW_B;
  (* 1 · 2 : 끝에서 3 초 재기 *)
  TA(IN := SENSOR_A, PT := T#3s);
  A_DONE := TA.Q;
  TB(IN := SENSOR_B, PT := T#3s);
  B_DONE := TB.Q;
  (* 3 · 4 : 3 초 뒤 출발 *)
  MOVE_RIGHT := (A_DONE OR MOVE_RIGHT) AND NOT SENSOR_B AND NOT MOVE_LEFT;
  MOVE_LEFT := (B_DONE OR MOVE_LEFT) AND NOT SENSOR_A AND NOT MOVE_RIGHT;
END_PROGRAM

CONFIGURATION Config0
  RESOURCE Res0 ON PLC
    TASK task0(INTERVAL := T#50ms, PRIORITY := 0);
    PROGRAM instance0 WITH task0 : conveyor;
  END_RESOURCE
END_CONFIGURATION
