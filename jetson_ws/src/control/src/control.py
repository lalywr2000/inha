import rospy
from geometry_msgs import Point


WALL_DRIVE_DIST = 1.1
WALL_DROP_DIST  = 0.8

WALL_DIST_NOISE_BAND = 0.2
INCLINE_ALIGN_NOISE_BAND = 0.3

mission_num = 1


def mission_1(distance, incline):  # Move Forward
	global mission_num
	if (mission_num == 1):

		if distance > WALL_DRIVE_DIST:
			# move forard
		else:
			# stop signal
			mission_num += 1

	return


# def mission_2(distance, incline):
# 	global mission_num
# 	if (mission_num == 2):
# 		pass
	
# 	return


def msgCallback(msg):
	mission_1(msg.x, msg.y)
	# mission_2(msg.x, msg.y)

	return


def sub():
	rospy.init_node('control_node', anonymous=True)
	rospy.Subscriber("/main_wall", Point, msgCallback)

	rospy.spin()


if __name__ == '__main__':
	sub()


# 2. control to keep the distance. go find wall to certain direction and make it stop.
# 3. consider the angle of the wall and make it align to the wall.
# 4. examine the 4 direction of the wall and follow the wall CCW.
