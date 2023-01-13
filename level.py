import pygame
from settings import *
from tile import Tile
from player import Player

class Level:
    def __init__(self):

        # level setup
        self.display_surface = pygame.display.get_surface()

        # sprite group setup
        self.visible_sprites = pygame.sprite.Group()
        self.active_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()

        self.setup_level()

    def setup_level(self):
        for row_index,row in enumerate(LEVEL_MAP):
            print(f'{row_index}:{row}')
            for col_index,col in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE
                if col == 'X':
                    Tile((x,y),[self.visible_sprites])
                if col == 'P':
                    Player((x,y),[self.visible_sprites])

    def run(self):
        # run the entire game (level)
        self.visible_sprites.draw(self.display_surface)