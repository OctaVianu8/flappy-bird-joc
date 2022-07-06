import pygame
from constants import *

pasareImg = pygame.image.load("sprites/redbird-midflap.png")
pasareImg = pygame.transform.scale(pasareImg,(BIRD_WIDTH,BIRD_HEIGHT))

backgroundImg = pygame.image.load("sprites/background-day.png")
backgroundImg = pygame.transform.scale(backgroundImg,(SCREEN_WIDTH,SCREEN_HEIGHT))

pipe_down = pygame.image.load("sprites/pipe-green.png")
pipe_up = pygame.transform.rotate(pipe_down, 180)

pipe_down = pygame.transform.scale(pipe_down, (PIPE_WIDTH, PIPE_HEIGHT))
pipe_up = pygame.transform.scale(pipe_up, (PIPE_WIDTH, PIPE_HEIGHT))

cifre_sprite = []
for i in range(0, 10):
    drum_cifra = "sprites/" + str(i) + ".png"
    cifra_img = pygame.image.load(drum_cifra)
    cifre_sprite.append(cifra_img)