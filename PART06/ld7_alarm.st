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
    CNT_RST  AT %QX2.6 : BOOL;     (* 카운트 초기화 *)
    COUNT    AT %MW0   : INT;      (* 왕복 횟수 *)
    CNT : CTU;
    ALM_RST  AT %QX2.5 : BOOL;     (* 알람 리셋 — HMI 에서도 같은 주소(코일 21) *)
    ALARM    AT %QX3.1 : BOOL;     (* 알람 — 리셋 전까지 1 유지 (코일 25) *)
    BLINK    AT %QX3.2 : BOOL;     (* 알람 깜빡임 — HMI 램프용 (코일 26) *)
    T_LOST : TON;                  (* 움직이는데 센서가 박스를 못 본 시간 *)
    T_ON : TON;                    (* 깜빡이 — 켜짐 시간 *)
    T_OFF : TON;                   (* 깜빡이 — 꺼짐 시간 *)
  END_VAR
  (* 0 : 센서 뒤집기 — D0 는 감지 = 0 이므로 NOT 으로 1 = 감지 *)
  SENSOR_A := NOT RAW_A;
  SENSOR_B := NOT RAW_B;
  (* 1 : 왕복 횟수 *)
  CNT(CU := SENSOR_A AND MOVE_LEFT, R := CNT_RST, PV := 9999);
  COUNT := CNT.CV;
  (* 2 : 모터가 도는데 10 초 동안 A · B 어느 센서도 박스를 못 보면 *)
  T_LOST(IN := (MOVE_RIGHT OR MOVE_LEFT) AND NOT SENSOR_A AND NOT SENSOR_B,
         PT := T#10s);
  (* 3 : 알람 자기유지 — ALM_RST 로만 풀림 *)
  ALARM := (T_LOST.Q OR ALARM) AND NOT ALM_RST;
  (* 4 · 5 : 끝에서 3 초 — 알람 중에는 재지 않음 *)
  TA(IN := SENSOR_A AND NOT ALARM, PT := T#3s);
  A_DONE := TA.Q;
  TB(IN := SENSOR_B AND NOT ALARM, PT := T#3s);
  B_DONE := TB.Q;
  (* 6 · 7 : 출발 — 알람이면 정지 *)
  MOVE_RIGHT := (A_DONE OR MOVE_RIGHT) AND NOT SENSOR_B
                AND NOT MOVE_LEFT AND NOT ALARM;
  MOVE_LEFT := (B_DONE OR MOVE_LEFT) AND NOT SENSOR_A
               AND NOT MOVE_RIGHT AND NOT ALARM;
  (* 8 · 9 · 10 : 알람 깜빡이 (0.5 초 켜짐 · 0.5 초 꺼짐) *)
  T_ON(IN := ALARM AND NOT T_OFF.Q, PT := T#500ms);
  T_OFF(IN := T_ON.Q, PT := T#500ms);
  BLINK := ALARM AND NOT T_ON.Q;
END_PROGRAM

CONFIGURATION Config0
  RESOURCE Res0 ON PLC
    TASK task0(INTERVAL := T#50ms, PRIORITY := 0);
    PROGRAM instance0 WITH task0 : conveyor;
  END_RESOURCE
END_CONFIGURATION
