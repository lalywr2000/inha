from gamepad_controller import ShanWanGamepad
from mecanumwheel import SerialComm
import math

if __name__ == '__main__':
    shanwan_gamepad = ShanWanGamepad()
    robot = SerialComm(port='/dev/ttyACM0', baudrate=9600, timeout=1)

    try:
        while True:
            gamepad_input = shanwan_gamepad.read_data()

            LH = gamepad_input.analog_stick_left.x  # Left joystick Horizontal direction
            LV = gamepad_input.analog_stick_left.y  # Left joystick Vertical direction
            RH = gamepad_input.analog_stick_right.y * -1.0  # Right joystick Horizontal direction
            A = gamepad_input.button_a

            # Remove noise value
            LH = 0.0 if -0.1 < LH < 0.1 else LH
            LV = 0.0 if -0.1 < LV < 0.1 else LV
            RH = 0.0 if -0.1 < RH < 0.1 else RH

            # Left joystick: parallel movement to 8 directions
            # Right joystick: rotation in place
            # [left joystick has priority to control]

            if LH == 0 and LV > 0:

                speed = LV * 5.0
                angle = 90.0

                if RH > 0:
                    print("direction 1 clockwise rotation")
                    rotation = -1.0

                elif RH < 0:
                    print("direction 1 counter-clockwise rotation")
                    rotation = 1.0

                else:
                    print("direction 1 no rotation")
                    rotation = 0.0


            elif LH > 0 and LV > 0:
                speed = math.sqrt(LV ** 2.0 + LH ** 2.0) * 5.0
                angle = 45.0

                if RH > 0:
                    print("direction 2 clockwise rotation")
                    rotation = -1.0

                elif RH < 0:
                    print("direction 2 counter-clockwise rotation")
                    rotation = 1.0

                else:
                    print("direction 2 no rotation")
                    rotation = 0.0

            elif LH > 0 and LV == 0:
                speed = math.sqrt(LV ** 2.0 + LH ** 2.0) * 5.0
                angle = 0.0

                if RH > 0:
                    print("direction 3 clockwise rotation")
                    rotation = -1.0

                elif RH < 0:
                    print("direction 3 counter-clockwise rotation")
                    rotation = 1.0

                else:
                    print("direction 3 no rotation")
                    rotation = 0.0

            elif LH > 0 and LV < 0:
                speed = math.sqrt(LV ** 2.0 + LH ** 2.0) * 5.0
                angle = 315.0

                if RH > 0:
                    print("direction 4 clockwise rotation")
                    rotation = -1.0

                elif RH < 0:
                    print("direction 4 counter-clockwise rotation")
                    rotation = 1.0

                else:
                    print("direction 4 no rotation")
                    rotation = 0.0

            elif LH == 0 and LV < 0:
                speed = math.sqrt(LV ** 2.0 + LH ** 2.0) * 5.0
                angle = 270.0

                if RH > 0:
                    print("direction 5 clockwise rotation")
                    rotation = -1.0

                elif RH < 0:
                    print("direction 5 counter-clockwise rotation")
                    rotation = 1.0

                else:
                    print("direction 5 no rotation")
                    rotation = 0.0

            elif LH < 0 and LV < 0:
                speed = math.sqrt(LV ** 2.0 + LH ** 2.0) * 5.0
                angle = 225.0

                if RH > 0:
                    print("direction 6 clockwise rotation")
                    rotation = -1.0

                elif RH < 0:
                    print("direction 6 counter-clockwise rotation")
                    rotation = 1.0

                else:
                    print("direction 6 no rotation")
                    rotation = 0.0

            elif LH < 0 and LV == 0:
                speed = math.sqrt(LV ** 2.0 + LH ** 2.0) * 5.0
                angle = 180.0

                if RH > 0:
                    print("direction 7 clockwise rotation")
                    rotation = -1.0

                elif RH < 0:
                    print("direction 7 counter-clockwise rotation")
                    rotation = 1.0

                else:
                    print("direction 7 no rotation")
                    rotation = 0.0

            elif LH < 0 and LV > 0:
                speed = math.sqrt(LV ** 2.0 + LH ** 2.0) * 5.0
                angle = 135.0

                if RH > 0:
                    print("direction 8 clockwise rotation")
                    rotation = -1.0

                elif RH < 0:
                    print("direction 8 counter-clockwise rotation")
                    rotation = 1.0

                else:
                    print("direction 8 no rotation")
                    rotation = 0.0

            elif LH == 0 and LV == 0:
                speed = 0.0
                angle = 90.0

                if RH > 0:
                    print("direction 9 clockwise rotation")
                    rotation = -1.0

                elif RH < 0:
                    print("direction 9 counter-clockwise rotation")
                    rotation = 1.0

                else:
                    print("direction 9 no rotation")
                    rotation = 0.0

            if A == 1:
                robot.kill()

            robot.move_data(speed, angle, rotation)

    except KeyboardInterrupt:
        pass

    finally:
        robot.kill()
        robot.close()


