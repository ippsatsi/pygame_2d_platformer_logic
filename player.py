import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.Surface((TILE_SIZE//2, TILE_SIZE))
        self.image.fill(PLAYER_COLOR)
        
        # player movement
        self.direction = pygame.math.Vector2()
        self.speed = 8

def input(self):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        self.direction.x = 1
    elif keys[pygame.K_LEFT]:
        self.direction.x = -1
    else:
        self.direction = 0