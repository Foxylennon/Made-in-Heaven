import pygame,math
from pygame import*
from math import*


#button class
class Button():
    def __init__(self, x, y, image, image2, scale, screen_width) -> None:
        # Calculate dynamic width as a percentage of screen width (e.g., 10%)
        button_width = screen_width * scale
        button_height = button_width * (image.get_height() / image.get_width())  # Keep aspect ratio

        # Scale images
        self.image = pygame.transform.scale(image, (int(button_width), int(button_height)))
        self.image2 = pygame.transform.scale(image2, (int(button_width), int(button_height)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def set_position(self, x, y):
        #Update the button's position dynamically
        self.rect.topleft = (x, y)

    #draw button 
    def draw(self,surface):
        action = False
        mouse_over = False

        #mouse position
        pos = mouse.get_pos()

        #check mouse over and clicked conditions
        if self.rect.collidepoint(pos):
            mouse_over = True
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        #display button
        if mouse_over == False:
            surface.blit(self.image, (self.rect.x, self.rect.y))
        elif mouse_over == True:
            surface.blit(self.image2, (self.rect.x, self.rect.y))

        return action
    
    