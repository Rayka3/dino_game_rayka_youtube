import pygame
from pygame import *


class pterodactile(sprite.Sprite):
    def __init__(self, speed):
        sprite.Sprite.__init__(self)
        #self.image = Surface((50, 30))
        #self.image.fill(Color('yellow'))
        self.image = image.load('textures/pter.png')
        self.rect = Rect(1110, 500, 30, 30)
        self.speed = speed
        
    def update(self):
        
        self.rect.x -= self.speed
        if self.rect.x <= -30:
            del(self)
        
