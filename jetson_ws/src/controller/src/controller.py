import math

import rospy
from std_msgs.msg import String

from gamepad_controller import ShanWanGamepad
from mecanumwheel import SerialComm


rospy.init_node('controller_node', anonymous=True)
pub = rospy.Publisher('/stepper/input', String, queue_size=1)
msg = String()

shanwan_gamepad = ShanWanGamepad()

robot = SerialComm(port='/dev/ttyACM0', baudrate=9600, timeout=1)


while True:
    gamepad_input = shanwan_gamepad.read_data()

    LH = gamepad_input.analog_stick_left.x  # Left joystick Horizontal direction
    LV = gamepad_input.analog_stick_left.y  # Left joystick Vertical direction
    RH = gamepad_input.analog_stick_right.y * -1.0  # Right joystick Horizontal direction

    # Remove noise value
    LH = 0.0 if -0.1 < LH < 0.1 else LH
    LV = 0.0 if -0.1 < LV < 0.1 else LV
    RH = 0.0 if -0.1 < RH < 0.1 else RH

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

    robot.move_data(speed, angle, rotation)


    x = gamepad_input.button_x
    a = gamepad_input.button_a
    b = gamepad_input.button_b
    y = gamepad_input.button_y

    if x:
        print('x')
        msg.data = "0,0,1,0,0,0\n"
    if y:
        print('y')
        msg.data = "0,0,0,1,0,0\n"
    if a:
        print('a')
        msg.data = "???"
    if b:
        print('b')
        msg.data = "???"

    pub.publish(msg)
