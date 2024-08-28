import sys
import time
import math
import pygame
import backend
import collections

pygame.init()
screen = pygame.display.set_mode((480, 640))
pygame.display.set_caption("대화형 시간표 마법사")
giant_text = pygame.font.SysFont("arialblack", 45)
big_text = pygame.font.SysFont("malgungothic", 24)
small_text = pygame.font.SysFont("malgungothic", 16)
tiny_text = pygame.font.SysFont("malgungothic", 12)
micro_text = pygame.font.SysFont("malgungothic", 10)
sleep_time = 0.1

# 이미지 업로드 (home_page)
home_background_img = pygame.image.load(backend.dir + r'/object/home_background.jpg').convert_alpha()
login_img = pygame.image.load(backend.dir + r'/object/login.jpg').convert_alpha()
register_img = pygame.image.load(backend.dir + r'/object/register.jpg').convert_alpha()

# 이미지 업로드 (login_page & register_page)
pw_background_img = pygame.image.load(backend.dir + r'/object/pw_background.jpg').convert_alpha()


class Button:
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


class HomePage:
    def __init__(self):
        self.background = home_background_img
        self.button_list = []
        self.button_list.append(Button(60, 350, login_img))     # 로그인 버튼 (idx = 0)
        self.button_list.append(Button(240, 350, register_img))     # 가입하기 버튼 (idx = 1)
        self.text = ''
        self.color_off = pygame.Color('lightskyblue3')
        self.color_on = pygame.Color('grey15')
        self.blank = pygame.Rect(145, 250, 250, 80)
        self.issue = None

    def draw(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                elif len(self.text) < 8:
                    self.text += event.unicode

        screen.blit(self.background, (0, 0))
        if self.text:
            pygame.draw.rect(screen, self.color_on, self.blank, 2)
        else:
            pygame.draw.rect(screen, self.color_off, self.blank, 2)
        screen.blit(giant_text.render(self.text, True, (0, 0, 0)), (self.blank.x + 3, self.blank.y + 8))
        if self.issue == 'login':
            screen.blit(big_text.render("존재하지 않는 ID 입니다", True, (255, 80, 120)), (85, 205))
        if self.issue == 'register':
            screen.blit(big_text.render("이미 등록된 ID 입니다", True, (255, 80, 120)), (85, 205))

        next_page = None
        for i, button in enumerate(self.button_list):
            if button.draw():
                if i == 0:     # 로그인 버튼
                    file = open(backend.dir + r'/user_DB.txt', mode='r', encoding='UTF-8')
                    for line in file.read().strip().split('\n'):
                        temp = line.split('+')
                        if temp[0] == self.text:
                            self.issue = None
                            next_page = ('login_page', temp[0], temp[1])
                            break
                    else:
                        self.issue = 'login'
                    file.close()

                else:     # 가입하기 버튼
                    file = open(backend.dir + r'/user_DB.txt', mode='r', encoding='UTF-8')
                    for line in file.read().strip().split('\n'):
                        temp = line.split('+')
                        if temp[0] == self.text:
                            self.issue = 'register'
                            break
                    else:
                        self.issue = None
                        next_page = ('register_page', self.text)
                    file.close()

        return next_page
