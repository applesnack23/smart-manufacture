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
    HMI_AUTO   AT %QX2.0 : BOOL;   (* HMI 버튼 — Modbus 코일 16 *)
    HMI_MANUAL AT %QX2.1 : BOOL;   (* 코일 17 *)
    HMI_FWD    AT %QX2.2 : BOOL;   (* 수동 정방향 — 코일 18 *)
    HMI_REV    AT %QX2.3 : BOOL;   (* 수동 역방향 — 코일 19 *)
    HMI_STOP   AT %QX2.4 : BOOL;   (* 수동 정지 — 코일 20 *)
    AUTO       AT %QX3.0 : BOOL;   (* 1 = AUTO, 0 = MANUAL — 코일 24 *)
    AUTO_R : BOOL;                 (* 자동 정방향 *)
    AUTO_L : BOOL;
    MAN_R : BOOL;                  (* 수동 정방향 *)
    MAN_L : BOOL;
  END_VAR
  (* 0 : 센서 뒤집기 — D0 는 감지 = 0 이므로 NOT 으로 1 = 감지 *)
  SENSOR_A := NOT RAW_A;
  SENSOR_B := NOT RAW_B;
  (* 1 : AUTO 자기유지 — MANUAL 버튼이면 풀림 *)
  AUTO := (HMI_AUTO OR AUTO) AND NOT HMI_MANUAL;
  (* 2 · 3 : 자동 — 끝에서 3 초 *)
  TA(IN := SENSOR_A AND AUTO, PT := T#3s);
  A_DONE := TA.Q;
  TB(IN := SENSOR_B AND AUTO, PT := T#3s);
  B_DONE := TB.Q;
  (* 4 · 5 : 자동 운전 *)
  AUTO_R := (A_DONE OR AUTO_R) AND NOT SENSOR_B AND NOT AUTO_L AND AUTO;
  AUTO_L := (B_DONE OR AUTO_L) AND NOT SENSOR_A AND NOT AUTO_R AND AUTO;
  (* 6 · 7 : 수동 운전 — 끝 센서에서 스스로 멈춤 *)
  MAN_R := (HMI_FWD OR MAN_R) AND NOT HMI_STOP AND NOT SENSOR_B
           AND NOT MAN_L AND NOT AUTO;
  MAN_L := (HMI_REV OR MAN_L) AND NOT HMI_STOP AND NOT SENSOR_A
           AND NOT MAN_R AND NOT AUTO;
  (* 8 · 9 : 출력 = 자동 또는 수동 *)
  MOVE_RIGHT := (AUTO_R OR MAN_R);
  MOVE_LEFT := (AUTO_L OR MAN_L);
END_PROGRAM

CONFIGURATION Config0
  RESOURCE Res0 ON PLC
    TASK task0(INTERVAL := T#50ms, PRIORITY := 0);
    PROGRAM instance0 WITH task0 : conveyor;
  END_RESOURCE
END_CONFIGURATION
