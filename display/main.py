import os
import sys
import time
import pygame

dir = os.getcwd()

pygame.init()
pygame.display.set_caption("inha application")
screen = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
text = pygame.font.SysFont("bold", 75)


display_img = pygame.image.load(dir + r'/object/display.png').convert_alpha()

scale_factor = 0.43

display_img = pygame.transform.scale(display_img, (int(display_img.get_size()[0] * scale_factor), int(display_img.get_size()[1] * scale_factor)))
    

class Page:
    def draw(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(display_img, (0, 0))

        # screen.blit(text.render("asdfasdf", True, (0, 0, 0)), (97, 263))

        # screen.fill((255, 255, 255))
        # pygame.draw.rect(screen, (0, 0, 0), (0, 0, 20, 20))
        # pygame.draw.rect(screen, (0, 0, 0), (1260, 700, 20, 20))

        return


page = Page()

while True:
    page.draw()
    pygame.display.update()
