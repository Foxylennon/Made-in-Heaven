import pygame,math,button,background
from pygame import *
from math import*
from button import*
from background import*



pygame.init()
pygame.display.set_caption("Made in Heaven")
screen = pygame.display.set_mode((0,0),pygame.RESIZABLE)
screen_width , screen_height = screen.get_size() 


screen_state = "main"   #main, game, options

background = Background('fond_écran.png', [0,0])

clicked = False

#title image
title_img = image.load('titre_image.png').convert_alpha()
#dynamic title
title_scale = 0.55
title_width = screen_width * title_scale #title size in % of the screen
title_height = title_width * (title_img.get_height() / title_img.get_width())
title_img_dynamic = transform.scale(title_img, (int(title_width), int(title_height)))

#button image
exit_img = image.load('quit_button.png').convert_alpha()
exit_img2 = image.load('quit_button_2.png').convert_alpha()
play_img = image.load('play_button.png').convert_alpha()
play_img2 = image.load('play_button_2.png').convert_alpha()
options_img = image.load('options_button.png').convert_alpha()
options_img2 = image.load('options_button_2.png').convert_alpha()
back_img = image.load('back_button.png').convert_alpha()
back_img2 = image.load('back_button_2.png').convert_alpha()

#cursor image
new_cursor = image.load('curseur.png').convert_alpha()

#hide mouse cursor
mouse.set_visible(False)


#create button
button_scale = 0.14
exit_button = Button(1000,0,exit_img,exit_img2,button_scale,screen_width)
options_button = Button(0,0,options_img,options_img2,button_scale,screen_width)
play_button = Button(0,0,play_img,play_img2,button_scale,screen_width)
back_button = Button(0,0,back_img,back_img2,button_scale,screen_width)

def update_button_positions(screen_width, screen_height):   #Update button positions relative to the screen size.
    
    button_width = exit_button.rect.width

    # Center the buttons horizontally and set them at relative vertical positions
    exit_button.set_position(screen_width / 2 - button_width / 2, screen_height * 0.8)
    play_button.set_position(screen_width / 2 - button_width / 2, screen_height * 0.4)
    options_button.set_position(screen_width / 2 - button_width / 2, screen_height * 0.6)
    back_button.set_position(screen_width / 2 - button_width / 2, screen_height * 0.8)

update_button_positions(screen_width, screen_height)

def get_dynamic_title_position(screen_width, screen_height):
    title_x = screen_width / 2 - title_width / 2  # Center horizontally
    title_y = screen_height * 0.1 - (title_height / 2) * 0.85  # Set at 10% down the screen height
    return title_x, title_y

#game loop

