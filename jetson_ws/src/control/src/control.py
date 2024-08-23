import rospy
from geometry_msgs import Point

from mecanumwheel import SerialComm


WALL_DRIVE_DIST = 1.1
WALL_DROP_DIST  = 0.8

WALL_DIST_NOISE_BAND = 0.2
INCLINE_ALIGN_NOISE_BAND = 0.3

FRONT_WALL_PARALLEL_CONDITION = 0.1

DRIVE_SPEED = 3.0


robot = SerialComm(port='/dev/ttyACM0', baudrate=9600, timeout=1)

mission_num = 1


# speed [km/h], angle [deg], rotation [-1.0: CW, 0.0: N/A, 1.0: CCW]


def mission_1(distance, incline):  # move forward to the wall
	global mission_num
	if (mission_num == 1):

		if distance > WALL_DRIVE_DIST:
			speed = DRIVE_SPEED
			angle = 90.0
			if incline > FRONT_WALL_PARALLEL_CONDITION:
				rotation = 1.0
			elif incline < -1.0 * FRONT_WALL_PARALLEL_CONDITION:
				rotation = -1.0
			else:
				rotation = 0.0
            
			robot.move_data(speed, angle, rotation)
		
		else:
			speed = 0.0
			angle = 90.0
			rotation = 0.0
            
			robot.move_data(speed, angle, rotation)
			mission_num += 1

	return


# def mission_2(distance, incline):  # Turn Left
# 	global mission_num
# 	if (mission_num == 2):
# 		pass
	
# 	return


# def mission_3(distance, incline):  # Move Forward
# 	global mission_num
# 	if (mission_num == 3):
# 		pass
	
# 	return


def msgCallback(msg):
	mission_1(msg.x, msg.y)
	# mission_2(msg.x, msg.y)
    # mission_3(msg.x, msg.y)

	return


def sub():
	rospy.init_node('control_node', anonymous=True)
	rospy.Subscriber("/main_wall", Point, msgCallback)

	try:
		rospy.spin()
	except KeyboardInterrupt:
		pass
	finally:
		robot.kill()
		robot.close()


if __name__ == '__main__':
	sub()
