import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,groups,collision_sprites):
        super().__init__(groups)
        self.image = pygame.Surface((TILE_SIZE // 2,TILE_SIZE))
        self.image.fill(PLAYER_COLOR)
        self.rect = self.image.get_rect(topleft = pos)
        
        # player movement
        self.direction = pygame.math.Vector2()
        self.speed = 8
        self.gravity = 0.8
        self.jump_speed = 16
        self.collision_sprites = collision_sprites

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE]:
            self.direction.y = -self.jump_speed

    def horizontal_collision(self):
        for sprite in self.collision_sprites.sprites():
            if sprite.rect.colliderect(self.rect):
                # si hay colision, averiguamos si la direccion
                # del jugador es hacia la izquierda, en ese caso
                # la colision es por la izq. del jugador contra la
                # derecha del sprite
                if self.direction.x < 0:
                    self.rect.left = sprite.rect.right
                if self.direction.x > 0:
                    self.rect.right = sprite.rect.left


    def vertical_collision(self):
        for sprite in self.collision_sprites.sprites():
            if sprite.rect.colliderect(self.rect):
                # si hay colision, averiguamos si la direccion
                # del jugador es hacia arriba, en ese caso
                # la colision es por la parte sup. del jugador contra
                # la parte inferior del sprite
                if self.direction.y < 0:
                    self.rect.top = sprite.rect.bottom
                    # para q no se quede pegado al techo
                    self.direction.y = 0
                if self.direction.y > 0:
                    self.rect.bottom = sprite.rect.top
                    # para q no se vaya acumulando la gravedad
                    # aunque el jugador no siga cayendo
                    self.direction.y = 0

    def apply_gravity(self):
        # la direccion vertical sera afectada por la gravedad
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def update(self):
        self.input()
        self.rect.x += self.direction.x * self.speed
        self.horizontal_collision()
        
        self.apply_gravity()
        self.vertical_collision()