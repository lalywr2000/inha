import os
import sys
import time
import pygame

dir = os.getcwd()

pygame.init()
pygame.display.set_caption("inha application")
screen = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
text = pygame.font.SysFont("bold", 75)


background_img = pygame.image.load(dir + r'/object/background.png').convert_alpha()

scale_factor = 0.46

background_img = pygame.transform.scale(background_img, (int(background_img.get_size()[0] * scale_factor), int(background_img.get_size()[1] * scale_factor)))
    

class Page:
    def draw(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # screen.blit(background_img, (25, 0))

        # screen.blit(text.render("asdfasdf", True, (0, 0, 0)), (97, 263))

        screen.fill((255, 255, 255))
        pygame.draw.rect(screen, (0, 0, 0), (0, 0, 20, 20))

        return


page = Page()

while True:
    page.draw()
    pygame.display.update()
