import pygame
import global_values as gval

class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('files/bird.png')
        self.img_copy = self.image
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.vel = 0
        self.clicked = False
        self.downclicked = False

    def update(self):
        if gval.flying == True:
            self.vel += gval.gravity
            if self.vel > gval.map_bottom:
                self.vel = gval.map_bottom
            if self.rect.bottom < gval.screen_height:
                self.rect.y += int(self.vel)

        if gval.game_over == False:
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                self.vel = gval.rise_up
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
            if pygame.mouse.get_pressed()[2] == 1 and self.downclicked == False:
                self.downclicked = True
                self.vel = gval.fall_down
            if pygame.mouse.get_pressed()[2] == 0:
                self.downclicked = False

            self.image = self.img_copy

            self.image = pygame.transform.rotate(self.img_copy, self.vel * -2)
        else:
            self.image = pygame.transform.rotate(self.img_copy, gval.death)