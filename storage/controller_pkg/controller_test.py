from gamepad_controller import ShanWanGamepad

if __name__ == '__main__':

	shanwan_gamepad = ShanWanGamepad()

	while True:
		gamepad_input = shanwan_gamepad.read_data()

		throttle = gamepad_input.analog_stick_right.y
		steering = gamepad_input.analog_stick_left.x
		l1 = gamepad_input.button_l1
		l2 = gamepad_input.button_l2
		r1 = gamepad_input.button_r1
		r2 = gamepad_input.button_r2
		x = gamepad_input.button_x
		a = gamepad_input.button_a
		b = gamepad_input.button_b
		y = gamepad_input.button_y
		select = gamepad_input.button_select
		start = gamepad_input.button_start
		home = gamepad_input.button_home

		print('---------------')
		print(f'throttle={throttle}')
		print(f'steering={steering}')
		print(f'l1={l1}')
		print(f'l2={l2}')
		print(f'r1={r1}')
		print(f'r2={r2}')
		print(f'x={x}')
		print(f'a={a}')
		print(f'b={b}')
		print(f'y={y}')
		print(f'select={select}')
		print(f'start={start}')
		print(f'home={home}')
		print('---------------')