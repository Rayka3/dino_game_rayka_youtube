import pygame
from pygame import *


class dino(sprite.Sprite):
    def __init__(self, height, width, texture, x_start, y_start, speed):
        sprite.Sprite.__init__(self)
        self.image = Surface((width, height))
        #self.image.fill(Color('yellow'))
        self.image = image.load('textures/dino.png')
        self.rect = Rect(x_start, y_start, width, height)
        self.speed = speed
        self.jump_speed = 20
        self.gravity = 2
        self.direct = 'stay'

    def update(self, floor, enemies):
        if self.direct == 'jump':
            self.rect.y -= self.jump_speed
            self.jump_speed -= self.gravity
        self.collide(floor, enemies)
            

    def collide(self, floor, enemies):
        if sprite.collide_rect(self, floor):
            self.direct = 'stay'
            self.jump_speed = 20
            self.rect.y = floor.rect.y - 100
        for en in enemies:
            if sprite.collide_rect(self, en):
                self.speed = 0
                self.jump_speed = 0
                en.speed = 0
                self.direct = 'endgame'
        
        
