import pygame
import global_values as gval

class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('files/pipe.png')
        self.rect = self.image.get_rect()

        if position == 1: # pipe on top
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y - gval.pipe_gap / 2]
        if position == -1: # pipe on bottom
            self.rect.topleft = [x, y + gval.pipe_gap / 2]

    def update(self):
        self.rect.x -= gval.scroll_speed
        if self.rect.right < 0:
            self.kill()
