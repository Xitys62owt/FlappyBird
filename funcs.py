import pygame
import global_values as gval

screen = pygame.display.set_mode((gval.screen_width, gval.screen_height))
pygame.display.set_caption('Flappy Bird')

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

def reset_game(pipe_group, flappy):
    pipe_group.empty()
    flappy.rect.x = gval.x_start
    flappy.rect.y = gval.screen_height / 2
    gval.score = 0
    return gval.score