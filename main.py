from audioop import reverse
import random
from telnetlib import GA
from turtle import width
import pygame
from constants import *
from sprites import *

pygame.init()
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()
win = pygame.display.set_mode(SIZE)

xpipe = [500,800,1100]
ypipe = [-150,-200,-250]

pasare = pasareImg

speed =-5 
acceleration =1
x = SCREEN_WIDTH/4
y = SCREEN_HEIGHT/2

def afiseaza_scor():
    global scor

    cifre = []
    copie = scor
    while (copie != 0):
        cifre.append(copie % 10)
        copie = copie // 10

    if (len(cifre) == 0): cifre.append(0)
    cifre.reverse()

    L = 0
    for i in range(len(cifre)):
        L = L + cifre_sprite[cifre[i]].get_width()

    xCifra = SCREEN_WIDTH - L - 50
    yCifra = 50

    for i in range(len(cifre)):
        win.blit(cifre_sprite[cifre[i]], (xCifra, yCifra))
        xCifra += cifre_sprite[cifre[i]].get_width()

def deseneaza() :
    win.fill((0,0,0))
    win.blit(backgroundImg, (0,0))
    for i in range(3):
        win.blit(pipe_up,(xpipe[i],ypipe[i]))
        win.blit(pipe_down,(xpipe[i],ypipe[i]+pipe_up.get_height() + GAP))
    pasare = pygame.transform.rotate(pasareImg,-speed)
    win.blit(pasare, (x,y))
    afiseaza_scor()
    pygame.display.update()

def updatePipes():
    global xpipe
    for i in range(3) :
        xpipe[i] = xpipe[i] + pipeSpeed
        if (xpipe[i] + PIPE_WIDTH<0) : 
            xpipe[i] = SCREEN_WIDTH
            ypipe[i] = random.randint(-350,0)   

def verificaMoarte():
    pasare_drept = pygame.Rect(x, y, BIRD_WIDTH, BIRD_HEIGHT)

    for i in range(3):
        xSus, ySus = xpipe[i], ypipe[i]
        xJos, yJos = xpipe[i], ypipe[i] + PIPE_HEIGHT + GAP

        sus_drept = pygame.Rect(xSus, ySus, PIPE_WIDTH, PIPE_HEIGHT)
        jos_drept = pygame.Rect(xJos, yJos, PIPE_WIDTH, PIPE_HEIGHT)

        if (pasare_drept.colliderect(sus_drept) or pasare_drept.colliderect(jos_drept)):
            pygame.quit()

scor = 0
def verificaPunct():
    global scor
    for i in range(3):
        if (abs(x - (xpipe[i] + PIPE_WIDTH // 2)) <= 2):
            scor = scor + 1
            print(scor)

def update() :
    updatePipes()
    verificaMoarte()
    verificaPunct()
    global y,speed,acceleration
    y = y+ speed
    speed +=acceleration

while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_SPACE : speed =-10
    update()
    deseneaza()
    clock.tick(24)