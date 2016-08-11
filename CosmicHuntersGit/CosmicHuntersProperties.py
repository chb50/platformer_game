import pygame

pygame.init()
#Color Pallet
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
gray = (145, 145, 145)

darkRed = (150,0,0)
#Fonts (WILL NOT BE COMICSANS)
smallFont = pygame.font.SysFont("comicsansms", 25)
medFont = pygame.font.SysFont("comicsansms", 50)
largeFont = pygame.font.SysFont("comicsansms", 80)

#display
displayWidth = 1200
displayHeight = 800
gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
clock = pygame.time.Clock() #will be used to control frame rate of game
