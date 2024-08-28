import os
import sys
import pygame


dir = os.getcwd()

pygame.init()
screen = pygame.display.set_mode((1028, 600))
pygame.display.set_caption("inha application")
# big_text = pygame.font.SysFont("malgungothic", 24)  # replace working font

background_img = pygame.image.load(dir + r'/object/background.png').convert_alpha()
sonon_img = pygame.image.load(dir + r'/object/sonon.png').convert_alpha()

scale_factor = 0.385

background_img = pygame.transform.scale(background_img, (int(background_img.get_size()[0] * scale_factor), int(background_img.get_size()[1] * scale_factor)))
sonon_img = pygame.transform.scale(sonon_img, (int(sonon_img.get_size()[0] * scale_factor), int(sonon_img.get_size()[1] * scale_factor)))










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


class Page:
    def __init__(self):
        pass
        self.button_list = []
        # self.button_list.append(Button(60, 350, login_img))
        # self.pkg_list = [0,0,0,0,0,0]  # condition of stuff

    def draw(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(background_img, (0, 0))
        screen.blit(sonon_img, (0, 0))

        for i, button in enumerate(self.button_list):
            if button.draw():
                if i == 0:     # 로그인 버튼
                    pass
        return


page = Page()
while True:
    page.draw()
    pygame.display.update()
