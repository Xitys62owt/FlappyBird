import pygame
import random
import global_values as gval
import funcs as funcs
import button as button_class
import bird as bird
import pipe as pipe

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((gval.screen_width, gval.screen_height))
pygame.display.set_caption('Flappy Bird')

background = pygame.image.load('files/bg.png')
button = pygame.image.load('files/restart.png')

bird_group = pygame.sprite.Group()
pipe_group = pygame.sprite.Group()

flappy = bird.Bird(100, int(gval.screen_height / 2))
bird_group.add(flappy)

button = button_class.Button(gval.screen_width / 2 - 120, gval.screen_height / 2 - 100, button)

run = True
while run:
    clock.tick(gval.fps)

    screen.blit(background, (0, 0))

    bird_group.draw(screen)
    bird_group.update()
    pipe_group.draw(screen)

    if len(pipe_group) > 0:
        if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left \
                and bird_group.sprites()[0].rect.right < pipe_group.sprites()[0].rect.right \
                and gval.pass_pipe == False:
            gval.pass_pipe = True
        if gval.pass_pipe == True:
            if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.right:
                gval.score += 1
                gval.pass_pipe = False

    funcs.draw_text(str(gval.score), gval.font, gval.score_color, gval.screen_width / 2 - 20, 20)

    if pygame.sprite.groupcollide(bird_group, pipe_group, False, False):
        gval.game_over = True

    if flappy.rect.top < 0:
        gval.game_over = True

    if flappy.rect.bottom >= gval.screen_height:
        gval.game_over = True
        gval.flying = False

    if gval.game_over == False and gval.flying == True:
        time_now = pygame.time.get_ticks()
        if time_now - gval.last_pipe > gval.pipe_frequency:
            pipe_height = random.randint(-100, 100)
            btm_pipe = pipe.Pipe(gval.screen_width, gval.screen_height / 2 + pipe_height, -1)
            top_pipe = pipe.Pipe(gval.screen_width, gval.screen_height / 2 + pipe_height, 1)
            pipe_group.add(btm_pipe)
            pipe_group.add(top_pipe)
            gval.last_pipe = time_now

        pipe_group.update()

    if gval.game_over == True:
        if button.draw() == True:
            gval.game_over = False
            gval.score = funcs.reset_game(pipe_group, flappy)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and gval.flying == False and gval.game_over == False:
            gval.flying = True

    pygame.display.update()

pygame.quit()