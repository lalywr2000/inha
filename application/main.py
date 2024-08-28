import os
import sys
import pygame


dir = os.getcwd()

pygame.init()
pygame.display.set_caption("inha application")
screen = pygame.display.set_mode((1028, 600))
text = pygame.font.SysFont("bold", 80)

background_img = pygame.image.load(dir + r'/object/background.png').convert_alpha()
soffoff_img = pygame.image.load(dir + r'/object/soffoff.png').convert_alpha()
soffon_img = pygame.image.load(dir + r'/object/soffon.png').convert_alpha()
sonoff_img = pygame.image.load(dir + r'/object/sonoff.png').convert_alpha()
sonon_img = pygame.image.load(dir + r'/object/sonon.png').convert_alpha()
boffoff_img = pygame.image.load(dir + r'/object/boffoff.png').convert_alpha()
boffon_img = pygame.image.load(dir + r'/object/boffon.png').convert_alpha()
bonoff_img = pygame.image.load(dir + r'/object/bonoff.png').convert_alpha()
bonon_img = pygame.image.load(dir + r'/object/bonon.png').convert_alpha()
zero_img = pygame.image.load(dir + r'/object/zero.png').convert_alpha()

scale_factor = 0.385

background_img = pygame.transform.scale(background_img, (int(background_img.get_size()[0] * scale_factor), int(background_img.get_size()[1] * scale_factor)))
soffoff_img = pygame.transform.scale(soffoff_img, (int(soffoff_img.get_size()[0] * scale_factor), int(soffoff_img.get_size()[1] * scale_factor)))
soffon_img = pygame.transform.scale(soffon_img, (int(soffon_img.get_size()[0] * scale_factor), int(soffon_img.get_size()[1] * scale_factor)))
sonoff_img = pygame.transform.scale(sonoff_img, (int(sonoff_img.get_size()[0] * scale_factor), int(sonoff_img.get_size()[1] * scale_factor)))
sonon_img = pygame.transform.scale(sonon_img, (int(sonon_img.get_size()[0] * scale_factor), int(sonon_img.get_size()[1] * scale_factor)))
boffoff_img = pygame.transform.scale(boffoff_img, (int(boffoff_img.get_size()[0] * scale_factor), int(boffoff_img.get_size()[1] * scale_factor)))
boffon_img = pygame.transform.scale(boffon_img, (int(boffon_img.get_size()[0] * scale_factor), int(boffon_img.get_size()[1] * scale_factor)))
bonoff_img = pygame.transform.scale(bonoff_img, (int(bonoff_img.get_size()[0] * scale_factor), int(bonoff_img.get_size()[1] * scale_factor)))
bonon_img = pygame.transform.scale(bonon_img, (int(bonon_img.get_size()[0] * scale_factor), int(bonon_img.get_size()[1] * scale_factor)))
zero_img = pygame.transform.scale(zero_img, (int(zero_img.get_size()[0] * scale_factor), int(zero_img.get_size()[1] * scale_factor)))


pkg_status = ['', '', '', '', '', '']
pkg_cursor = None


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
        pass
        self.button_list = []
        self.button_list.append(Button(35, 35, 115, 252))
        self.button_list.append(Button(150, 35, 115, 252))
        self.button_list.append(Button(290, 35, 115, 252))
        self.button_list.append(Button(405, 35, 115, 252))
        self.button_list.append(Button(35, 310, 242, 252))
        self.button_list.append(Button(277, 310, 242, 252))

    def draw(self):
        global pkg_cursor

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(background_img, (0, 0))

        if not pkg_status[0] and not pkg_status[1]:
            screen.blit(soffoff_img, (35, 35))
        elif not pkg_status[0] and pkg_status[1]:
            screen.blit(soffon_img, (35, 35))
        elif pkg_status[0] and not pkg_status[1]:
            screen.blit(sonoff_img, (35, 35))
        elif pkg_status[0] and pkg_status[1]:
            screen.blit(sonon_img, (35, 35))

        if not pkg_status[2] and not pkg_status[3]:
            screen.blit(soffoff_img, (290, 35))
        elif not pkg_status[2] and pkg_status[3]:
            screen.blit(soffon_img, (290, 35))
        elif pkg_status[2] and not pkg_status[3]:
            screen.blit(sonoff_img, (290, 35))
        elif pkg_status[2] and pkg_status[3]:
            screen.blit(sonon_img, (290, 35))

        if not pkg_status[4] and not pkg_status[5]:
            screen.blit(boffoff_img, (35, 310))
        elif not pkg_status[4] and pkg_status[5]:
            screen.blit(boffon_img, (35, 310))
        elif pkg_status[4] and not pkg_status[5]:
            screen.blit(bonoff_img, (35, 310))
        elif pkg_status[4] and pkg_status[5]:
            screen.blit(bonon_img, (35, 310))

        if pkg_cursor is not None:
            screen.blit(zero_img, (500, 200)) # no not this make it as button

        for i, button in enumerate(self.button_list):
            if button.draw():
                pkg_status[i] = '_'
                pkg_cursor = i

        return


page = Page()

while True:
    page.draw()
    pygame.display.update()

    # print(boffoff_img.get_size())



# screen.blit(text.render("1234", True, (255, 80, 120)), (0, 0))