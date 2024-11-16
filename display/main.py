import os
import sys
import time
import pygame
from datetime import datetime
import pytz

dir = os.getcwd()

pygame.init()
pygame.display.set_caption("inha application")
screen = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
small_text = pygame.font.SysFont("Arial", 50)
big_text = pygame.font.SysFont("Arial", 140)


display_img = pygame.image.load(dir + r'/object/display.png').convert_alpha()
warn1_img = pygame.image.load(dir + r'/object/warn1.png').convert_alpha()
warn2_img = pygame.image.load(dir + r'/object/warn2.png').convert_alpha()

scale_factor = 0.435

display_img = pygame.transform.scale(display_img, (int(display_img.get_size()[0] * scale_factor), int(display_img.get_size()[1] * scale_factor)))
warn1_img = pygame.transform.scale(warn1_img, (int(warn1_img.get_size()[0] * scale_factor), int(warn1_img.get_size()[1] * scale_factor)))
warn2_img = pygame.transform.scale(warn2_img, (int(warn2_img.get_size()[0] * scale_factor), int(warn2_img.get_size()[1] * scale_factor)))

warning = True
warn_screen = False


class Page:
    def draw(self):
        global warning, warn_screen

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(display_img, (0, 0))

        korea_timezone = pytz.timezone('Asia/Seoul')
        korea_time = datetime.now(korea_timezone)
        year = korea_time.year
        month = korea_time.month
        day = korea_time.day
        hour = korea_time.hour
        minute = korea_time.minute
        second = korea_time.second

        screen.blit(pygame.transform.rotate(small_text.render('{}. {}. {}.'.format(year, month, day),
        True, (255, 255, 255)), 90), (35, 370))
        if second % 2 == 0:
            screen.blit(pygame.transform.rotate(big_text.render(str(hour).zfill(2) + ':' + str(minute).zfill(2),
            True, (255, 255, 255)), 90), (100, 330))
        else:
            screen.blit(pygame.transform.rotate(big_text.render(str(hour).zfill(2) + ' ' + str(minute).zfill(2),
            True, (255, 255, 255)), 90), (100, 330))

        if warning:
            if warn_screen:
                screen.blit(warn1_img, (3, -56))
            else:
                screen.blit(warn2_img, (3, -56))

            time.sleep(0.5)
            warn_screen = not warn_screen

        return


page = Page()

while True:
    page.draw()
    pygame.display.update()






