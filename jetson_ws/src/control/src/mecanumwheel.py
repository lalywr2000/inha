# serial_comm.py
import serial
import math


class SerialComm:
    def __init__(self, port='/dev/ttyUSB0', baudrate=9600, timeout=1):
        self.ser = serial.Serial(port, baudrate, timeout=timeout)
        if self.ser.is_open:
            print("Serial port is open")

    def move_data(self, speed, angle, rotation):    #speed는 km/h 단위, angle은 좌표평면 상의 각, rotation은 -1, 0, 1 중 하나의 값(-1은 시계방향, 1은 반시계 방향, 0은 회전 없음 )
        
        rad = angle * (math.pi / 180.0)  # 각도를 라디안으로 변환

        vx = speed * math.cos(rad) * 1000.0 / (60.0 * 60.0)
        vy = speed * math.sin(rad) * 1000.0 / (60.0 * 60.0)

        a = 0.215  # 가로, 로봇 중심에서 휠 중심까지 거리(측정해서 입력)
        b = 0.425  # 세로, 로봇 중심에서 휠 축까지 거리 (측정해서 입력)
        r = 0.1275  # 휠 반지름(측정해서 입력)

        # 각 바퀴의 속도를 계산합니다. 회전 운동을 포함
        v1 = (-vx + vy + (math.pi * rotation * (a + b))) * 60.0 / (2.0 * math.pi) / r
        v2 = (vx + vy - (math.pi * rotation * (a + b))) * 60.0 / (2.0 * math.pi) / r
        v3 = (-vx + vy - (math.pi * rotation * (a + b))) * 60.0 / (2.0 * math.pi) / r
        v4 = (vx + vy + (math.pi * rotation * (a + b))) * 60.0 / (2.0 * math.pi) / r

        fr = (v1 + 500.0) / 1000.0 * 200.0 - 100.0
        fl = (v2 + 500.0) / 1000.0 * 200.0 - 100.0
        bl = (v3 + 500.0) / 1000.0 * 200.0 - 100.0
        br = (v4 + 500.0) / 1000.0 * 200.0 - 100.0

        #각 바퀴의 회전 속도를 시리얼 통신으로 보냄
        message = f"fr{int(fr)}\nfl{int(fl)}\nbl{int(bl)}\nbr{int(br)}\n"
        print(message)

        self.ser.write(message.encode())

    def kill(self):
        message = "kill\n"
        self.ser.write(message.encode())

    def close(self):
        self.ser.close()
        print("Serial port closed")
