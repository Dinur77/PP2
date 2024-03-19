import pygame, sys, math

pygame.init()

pygame.display.set_mode((600, 400))

pygame.display.set_caption("Mickey Clock")

pygame.display.set_icon(pygame.image.load("mickey.jpeg"))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()          




