import pygame

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ORANGE = (255, 197, 82)
class UserEvents:
    def __init__(self):
        pass
    def keydown_colors(self, event, color):
        if event.key == pygame.K_b:
            color = BLUE
        elif event.key == pygame.K_w:
            color = WHITE
        elif event.key == pygame.K_s:
            color = BLACK
        elif event.key == pygame.K_r:
            color = RED
        elif event.key == pygame.K_g:
            color = GREEN
        elif event.key == pygame.K_o:
            color = ORANGE
        return color

