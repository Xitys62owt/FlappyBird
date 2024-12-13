import pygame

pygame.init()

# consts:
# game
fps = 60
score_color = (128, 0, 128)
pipe_frequency = 1500

# funcs
x_start = 100

# pipe
pipe_gap = 150
scroll_speed = 4

# bird
gravity = 0.6
map_bottom = 8
death = -90
rise_up = -10
fall_down = +15

# for all
font = pygame.font.SysFont('arial', 70)
screen_width = 864
screen_height = 500

# cond values
flying = False
game_over = False
last_pipe = pygame.time.get_ticks() - pipe_frequency
pass_pipe = False
score = 0