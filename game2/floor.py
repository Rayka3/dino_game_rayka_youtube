import pygame
from pygame import *


class Floor(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.image = image.load('textures/surface.png')
        #self.image = Surface((1080, 40))
        #self.image.fill(Color('black'))
        self.rect = Rect(0, 600, 1080, 510)
