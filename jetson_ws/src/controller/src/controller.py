import rospy
from std_msgs.msg import String

from gamepad_controller import ShanWanGamepad


rospy.init_node('controller_node', anonymous=True)
pub = rospy.Publisher('/stepper/input', String, queue_size=1)
msg = String()

shanwan_gamepad = ShanWanGamepad()


while True:
	gamepad_input = shanwan_gamepad.read_data()

	x = gamepad_input.button_x
	a = gamepad_input.button_a
	b = gamepad_input.button_b
	y = gamepad_input.button_y

	if x:
		print('x')
		msg.data = "???"
	if y:
		print('y')
		msg.data = "???"
	if a:
		print('a')
		msg.data = "???"
	if b:
		print('b')
		msg.data = "???"

	pub.publish(msg)
