import pygame
from pygame import *
import random

class cactus(sprite.Sprite):
    def __init__(self, speed):
        sprite.Sprite.__init__(self)
        a = random.randint(1, 2)
        self.image = Surface((60, 40))
        #self.image.fill(Color('yellow'))
        self.image = image.load( 'textures/stone{0}.png'.format(a) )
        self.rect = Rect(1110, 570, 30, 30)
        self.speed = speed
        
    def update(self):
        
        self.rect.x -= self.speed
        if self.rect.x <= -30:
            del(self)
        
