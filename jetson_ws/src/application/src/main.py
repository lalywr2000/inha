import os
import sys
import time
import pygame

from mecanumwheel import SerialComm

import rospy
from std_msgs.msg import String
from geometry_msgs import Point


dir = os.getcwd()


pygame.init()
pygame.display.set_caption("inha application")
screen = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
text = pygame.font.SysFont("bold", 75)


background_img = pygame.image.load(dir + r'/object/background.png').convert_alpha()

soffoff_img = pygame.image.load(dir + r'/object/soffoff.png').convert_alpha()
soffon_img = pygame.image.load(dir + r'/object/soffon.png').convert_alpha()
sonoff_img = pygame.image.load(dir + r'/object/sonoff.png').convert_alpha()
sonon_img = pygame.image.load(dir + r'/object/sonon.png').convert_alpha()

boffoff_img = pygame.image.load(dir + r'/object/boffoff.png').convert_alpha()
boffon_img = pygame.image.load(dir + r'/object/boffon.png').convert_alpha()
bonoff_img = pygame.image.load(dir + r'/object/bonoff.png').convert_alpha()
bonon_img = pygame.image.load(dir + r'/object/bonon.png').convert_alpha()

one_img = pygame.image.load(dir + r'/object/one.png').convert_alpha()
two_img = pygame.image.load(dir + r'/object/two.png').convert_alpha()
three_img = pygame.image.load(dir + r'/object/three.png').convert_alpha()
four_img = pygame.image.load(dir + r'/object/four.png').convert_alpha()
five_img = pygame.image.load(dir + r'/object/five.png').convert_alpha()
six_img = pygame.image.load(dir + r'/object/six.png').convert_alpha()
seven_img = pygame.image.load(dir + r'/object/seven.png').convert_alpha()
eight_img = pygame.image.load(dir + r'/object/eight.png').convert_alpha()
nine_img = pygame.image.load(dir + r'/object/nine.png').convert_alpha()
zero_img = pygame.image.load(dir + r'/object/zero.png').convert_alpha()

cancel_img = pygame.image.load(dir + r'/object/cancel.png').convert_alpha()
ok_img = pygame.image.load(dir + r'/object/ok.png').convert_alpha()

move_img = pygame.image.load(dir + r'/object/move.png').convert_alpha()
run_img = pygame.image.load(dir + r'/object/run.png').convert_alpha()
origin_img = pygame.image.load(dir + r'/object/origin.png').convert_alpha()
stopoff_img = pygame.image.load(dir + r'/object/stopoff.png').convert_alpha()
stopon_img = pygame.image.load(dir + r'/object/stopon.png').convert_alpha()

scale_factor = 0.46

background_img = pygame.transform.scale(background_img, (int(background_img.get_size()[0] * scale_factor), int(background_img.get_size()[1] * scale_factor)))

soffoff_img = pygame.transform.scale(soffoff_img, (int(soffoff_img.get_size()[0] * scale_factor), int(soffoff_img.get_size()[1] * scale_factor)))
soffon_img = pygame.transform.scale(soffon_img, (int(soffon_img.get_size()[0] * scale_factor), int(soffon_img.get_size()[1] * scale_factor)))
sonoff_img = pygame.transform.scale(sonoff_img, (int(sonoff_img.get_size()[0] * scale_factor), int(sonoff_img.get_size()[1] * scale_factor)))
sonon_img = pygame.transform.scale(sonon_img, (int(sonon_img.get_size()[0] * scale_factor), int(sonon_img.get_size()[1] * scale_factor)))

boffoff_img = pygame.transform.scale(boffoff_img, (int(boffoff_img.get_size()[0] * scale_factor), int(boffoff_img.get_size()[1] * scale_factor)))
boffon_img = pygame.transform.scale(boffon_img, (int(boffon_img.get_size()[0] * scale_factor), int(boffon_img.get_size()[1] * scale_factor)))
bonoff_img = pygame.transform.scale(bonoff_img, (int(bonoff_img.get_size()[0] * scale_factor), int(bonoff_img.get_size()[1] * scale_factor)))
bonon_img = pygame.transform.scale(bonon_img, (int(bonon_img.get_size()[0] * scale_factor), int(bonon_img.get_size()[1] * scale_factor)))

one_img = pygame.transform.scale(one_img, (int(one_img.get_size()[0] * scale_factor), int(one_img.get_size()[1] * scale_factor)))
two_img = pygame.transform.scale(two_img, (int(two_img.get_size()[0] * scale_factor), int(two_img.get_size()[1] * scale_factor)))
three_img = pygame.transform.scale(three_img, (int(three_img.get_size()[0] * scale_factor), int(three_img.get_size()[1] * scale_factor)))
four_img = pygame.transform.scale(four_img, (int(four_img.get_size()[0] * scale_factor), int(four_img.get_size()[1] * scale_factor)))
five_img = pygame.transform.scale(five_img, (int(five_img.get_size()[0] * scale_factor), int(five_img.get_size()[1] * scale_factor)))
six_img = pygame.transform.scale(six_img, (int(six_img.get_size()[0] * scale_factor), int(six_img.get_size()[1] * scale_factor)))
seven_img = pygame.transform.scale(seven_img, (int(seven_img.get_size()[0] * scale_factor), int(seven_img.get_size()[1] * scale_factor)))
eight_img = pygame.transform.scale(eight_img, (int(eight_img.get_size()[0] * scale_factor), int(eight_img.get_size()[1] * scale_factor)))
nine_img = pygame.transform.scale(nine_img, (int(nine_img.get_size()[0] * scale_factor), int(nine_img.get_size()[1] * scale_factor)))
zero_img = pygame.transform.scale(zero_img, (int(zero_img.get_size()[0] * scale_factor), int(zero_img.get_size()[1] * scale_factor)))

cancel_img = pygame.transform.scale(cancel_img, (int(cancel_img.get_size()[0] * scale_factor), int(cancel_img.get_size()[1] * scale_factor)))
ok_img = pygame.transform.scale(ok_img, (int(ok_img.get_size()[0] * scale_factor), int(ok_img.get_size()[1] * scale_factor)))

move_img = pygame.transform.scale(move_img, (int(move_img.get_size()[0] * scale_factor), int(move_img.get_size()[1] * scale_factor)))
run_img = pygame.transform.scale(run_img, (int(run_img.get_size()[0] * scale_factor), int(run_img.get_size()[1] * scale_factor)))
origin_img = pygame.transform.scale(origin_img, (int(origin_img.get_size()[0] * scale_factor), int(origin_img.get_size()[1] * scale_factor)))
stopoff_img = pygame.transform.scale(stopoff_img, (int(stopoff_img.get_size()[0] * scale_factor), int(stopoff_img.get_size()[1] * scale_factor)))
stopon_img = pygame.transform.scale(stopon_img, (int(stopon_img.get_size()[0] * scale_factor), int(stopon_img.get_size()[1] * scale_factor)))


pkg_status = ['', '', '', '', '', '']
pkg_cursor = None


robot = SerialComm(port='/dev/ttyACM0', baudrate=9600, timeout=1)
lock = False
# speed [km/h], angle [deg], rotation [-1.0: CW, 0.0: N/A, 1.0: CCW]
speed, angle, rotation = None, None, None
DRIVE_SPEED = 3.0


rospy.init_node('application_node', anonymous=True)
pub = rospy.Publisher('/stepper/input', String, queue_size=1)
msg = String()


mission_num = 1
mission_speed = 5.0
mission_wall_distance = 1.0
cnt = 0

def msgCallback(msg):
    global mission_num, mission_speed, mission_wall_distance, cnt
    distance, incline = msg.x, msg.y

    if cnt > 1000:
        sys.exit()

    if (mission_num == 1):  # go straight
        if distance > mission_wall_distance:
            speed = mission_speed
            angle = 90.0
            rotation = 0.0
            robot.move_data(speed, angle, rotation)
        else:
            speed = 0.0
            angle = 90.0
            rotation = 0.0
            robot.move_data(speed, angle, rotation)

            mission_num += 1
            time.sleep(1)

    elif (mission_num == 2):  # rotate clockwise
        if not (-0.1 < incline < 0.1):
            speed = 0.0
            angle = 90.0
            rotation = -1.0
            robot.move_data(speed, angle, rotation)
        else:
            speed = 0.0
            angle = 90.0
            rotation = 0.0
            robot.move_data(speed, angle, rotation)

            mission_num += 1
            time.sleep(1)

    elif (mission_num == 3):  # go backward
        if mission_wall_distance - 0.25 < distance < mission_wall_distance + 0.25:
            speed = mission_speed
            angle = 270.0
            rotation = 0.0
            robot.move_data(speed, angle, rotation)
        elif mission_wall_distance - 0.25 > distance:
            speed = mission_speed
            angle = 270.0
            rotation = 1.0
            robot.move_data(speed, angle, rotation)
        elif distance > mission_wall_distance + 0.25:
            speed = mission_speed
            angle = 270.0
            rotation = -1.0
            robot.move_data(speed, angle, rotation)
        
        cnt += 1

    return


rospy.Subscriber("/main_wall", Point, msgCallback)


class Button:
    def __init__(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)
        self.pressed = False

    def draw(self):
        action = False

        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] and not self.pressed:
                self.pressed = True
                action = True

        if not pygame.mouse.get_pressed()[0]:
            self.pressed = False
            
        return action
   

class ImgButton:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.pressed = False

    def draw(self):
        action = False

        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] and not self.pressed:
                self.pressed = True
                action = True

        if not pygame.mouse.get_pressed()[0]:
            self.pressed = False

        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action
    

class Page:
    def __init__(self):
        self.button_list = []
        self.button_list.append(Button(65, 40, 137, 301))
        self.button_list.append(Button(65 + 137, 40, 137, 301))
        self.button_list.append(Button(370, 40, 137, 301))
        self.button_list.append(Button(370 + 137, 40, 137, 301))
        self.button_list.append(Button(65, 375, 290, 301))
        self.button_list.append(Button(65 + 290, 375, 290, 301))

    def draw(self):
        global pkg_cursor, lock, speed, angle, rotation, distance, incline
        speed, angle, rotation = 0.0, 90.0, 0.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(background_img, (25, 0))

        if not pkg_status[0] and not pkg_status[1]:
            screen.blit(soffoff_img, (65, 40))
        elif not pkg_status[0] and pkg_status[1]:
            screen.blit(soffon_img, (65, 40))
        elif pkg_status[0] and not pkg_status[1]:
            screen.blit(sonoff_img, (65, 40))
        elif pkg_status[0] and pkg_status[1]:
            screen.blit(sonon_img, (65, 40))

        if not pkg_status[2] and not pkg_status[3]:
            screen.blit(soffoff_img, (370, 40))
        elif not pkg_status[2] and pkg_status[3]:
            screen.blit(soffon_img, (370, 40))
        elif pkg_status[2] and not pkg_status[3]:
            screen.blit(sonoff_img, (370, 40))
        elif pkg_status[2] and pkg_status[3]:
            screen.blit(sonon_img, (370, 40))

        if not pkg_status[4] and not pkg_status[5]:
            screen.blit(boffoff_img, (65, 375))
        elif not pkg_status[4] and pkg_status[5]:
            screen.blit(boffon_img, (65, 375))
        elif pkg_status[4] and not pkg_status[5]:
            screen.blit(bonoff_img, (65, 375))
        elif pkg_status[4] and pkg_status[5]:
            screen.blit(bonon_img, (65, 375))

        screen.blit(text.render(pkg_status[0], True, (0, 0, 0)), (97, 263))
        screen.blit(text.render(pkg_status[1], True, (0, 0, 0)), (222, 263))
        screen.blit(text.render(pkg_status[2], True, (0, 0, 0)), (402, 263))
        screen.blit(text.render(pkg_status[3], True, (0, 0, 0)), (527, 263))
        screen.blit(text.render(pkg_status[4], True, (0, 0, 0)), (172, 597))
        screen.blit(text.render(pkg_status[5], True, (0, 0, 0)), (450, 597))

        if pkg_cursor is None:
            screen.blit(move_img, (772, 40))

        if pkg_cursor is None:
            self.button_list.append(Button(772 + 117, 40, 117, 117))  # up
            self.button_list.append(Button(772, 40 + 117, 117, 117))  # left
            self.button_list.append(Button(772 + 117 + 117, 40 + 117, 117, 117))  # right
            self.button_list.append(Button(772 + 117, 40 + 117 + 117, 117, 117))  # down

            self.button_list.append(ImgButton(683, 423, run_img))
            self.button_list.append(ImgButton(683, 562, origin_img))

            if lock:
                self.button_list.append(ImgButton(961, 562, stopon_img))
            else:
                self.button_list.append(ImgButton(961, 562, stopoff_img))

        if pkg_cursor is not None:
            self.button_list.append(ImgButton(767, 80, one_img))
            self.button_list.append(ImgButton(767 + 115, 80, two_img))
            self.button_list.append(ImgButton(767 + 230, 80, three_img))
            self.button_list.append(ImgButton(767, 220, four_img))
            self.button_list.append(ImgButton(767 + 115, 220, five_img))
            self.button_list.append(ImgButton(767 + 230, 220, six_img))
            self.button_list.append(ImgButton(767, 360, seven_img))
            self.button_list.append(ImgButton(767 + 115, 360, eight_img))
            self.button_list.append(ImgButton(767 + 230, 360, nine_img))
            self.button_list.append(ImgButton(767 + 115, 500, zero_img))

            self.button_list.append(ImgButton(686, 507, cancel_img))
            self.button_list.append(ImgButton(1014, 507, ok_img))

        for i, button in enumerate(self.button_list):
            if button.draw():

                if pkg_cursor is not None:

                    if 1 <= i - 5 <= 10:
                        if pkg_status[pkg_cursor][-1] == '_':
                            pkg_status[pkg_cursor] = pkg_status[pkg_cursor][:-1]

                        if len(pkg_status[pkg_cursor]) < 3:
                            pkg_status[pkg_cursor] += str((i - 5) % 10)

                        if len(pkg_status[pkg_cursor]) < 3:
                            pkg_status[pkg_cursor] += '_'

                        time.sleep(0.2)

                    elif i == 16:
                        pkg_status[pkg_cursor] = ''
                        pkg_cursor = None

                        time.sleep(0.3)

                    elif i == 17:
                        if pkg_status[pkg_cursor][-1] == '_':
                            pkg_status[pkg_cursor] = pkg_status[pkg_cursor][:-1]
                        pkg_cursor = None

                        time.sleep(0.3)

                elif pkg_cursor is None:

                    if 0 <= i <= 5:
                        pkg_cursor = i
                        pkg_status[pkg_cursor] = '_'

                    elif i == 6:  # up
                        speed = DRIVE_SPEED
                        angle = 90.0
                        rotation = 0.0

                    elif i == 7:  # left
                        speed = DRIVE_SPEED
                        angle = 180.0
                        rotation = 0.0

                    elif i == 8:  # right
                        speed = DRIVE_SPEED
                        angle = 0.0
                        rotation = 0.0

                    elif i == 9:  # down
                        speed = DRIVE_SPEED
                        angle = 270.0
                        rotation = 0.0

                    elif i == 10:  # run
                        ##################################################
                        # Switch to controller - Elevator
                        lock = not lock

                        ##################################################
                        # Autonomous driving - Hallway
                        rospy.spin()

                        ##################################################
                    elif i == 11:  # origin
                        msg.data = "a"
                        pub.publish(msg)

                        time.sleep(0.3)

                    elif i == 12:  # stop
                        lock = not lock

                        time.sleep(0.3)

        if not lock:
            robot.move_data(speed, angle, rotation)

        while len(self.button_list) > 6:
            self.button_list.pop()

        return


page = Page()

while True:
    page.draw()
    pygame.display.update()
