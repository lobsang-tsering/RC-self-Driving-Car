import pygame
import time

pygame.init()
height = 400 #pixels
width = 200 #pixels 

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

gameDisplay = pygame.display.set_mode((height,height)) #frames width and height
pygame.display.set_caption("Self driving Car")
clock  = pygame.time.Clock()
crashed = False 

marioImg = pygame.image.load('car.png')

def car(x,y):
    gameDisplay.blit(carImg, (x,y))

x = (width * 0.45)
y = (height * 0.8)
x_change = 0 
y_change = 0

def key_check():
    while not crashed : 
        keys = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            
            if event.type  == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                    keys.append('S')
                elif event.key ==  pygame.K_RIGHT:
                    x_change = 5
                    keys.append('F')
                elif event.key == pygame.K_DOWN:
                    y_change = 5
                    keys.append('D')
                elif event.key == pygame.K_UP:
                    y_change = -5
                    keys.append('E')       
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                elif event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    y_change = 0
        x+= x_change
        y+= y_change
        gameDisplay.fill(white)
        car(x,y) 
        pygame.display.update()#just update only the parameter thing
        clock.tick(60)
        return keys
    pygame.quit()
quit()