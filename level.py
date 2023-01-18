import pygame
from settings import *
from tile import Tile
from player import Player

class Level:
    def __init__(self):

        # level setup
        self.display_surface = pygame.display.get_surface()

        # sprite group setup
        self.visible_sprites = CameraGroup()
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
                    Tile((x,y),[self.visible_sprites,self.collision_sprites])
                if col == 'P':
                    self.player = Player((x,y),[self.visible_sprites, self.active_sprites],self.collision_sprites)


    def run(self):
        # run the entire game (level)
        self.active_sprites.update()
        self.visible_sprites.custom_draw(self.player)


class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2(100,300)

        # center camera setup
        self.half_w = self.display_surface.get_size()[0] // 2
        self.half_h = self.display_surface.get_size()[1] // 2

    def custom_draw(self,player):

        # obtener el offset del player, distancia hasta el centro
        self.offset.x = player.rect.centerx - self.half_w
        self.offset.y = player.rect.centery - self.half_h

        for sprite in self.sprites():
            # desplazamos todo lo demas en sentido contrario
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)