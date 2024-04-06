import pygame
import sys

sys.path.append(r"C:\Users\fadil\Documents\Projects\MemGame")
from main import *


def StartUp():
    Win = pygame.display.set_mode((WIDTH, HEIGHT))
    
    mousePos = [0, 0]

    count = 0
    
    run = True
    while run:
        clk.tick(FPS)
        pygame.display.update()
        Win.fill((115, 147, 179))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mousePos[0], mousePos[1] = pygame.mouse.get_pos()
                if (mousePos[0] > 234 and mousePos[0] < 521) and (mousePos[1] > 381 and mousePos[1] < 446):
                    MainFunc()
                    count+=1

        if count:
            break

        Win.blit(bg, (0,0))