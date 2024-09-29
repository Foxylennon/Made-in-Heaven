import pygame,math
from pygame import*
from math import*


screen = display.set_mode((0,0))
screen_width , screen_height = screen.get_size()




class Background(sprite.Sprite):
    def __init__(self, image_file, location):
        sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

        self.ground = transform.scale(self.image, (int(screen_width), int(screen_height)))