import pygame
from CosmicHuntersProperties import *
from CosmicHuntersClasses import *

def testSurface():
    running = True
    
    gameDisplay.fill(white)
    floor = Boundary(0,600,displayWidth,200,0,0,color = darkRed)
    floor.renderBoundary()
    pygame.display.update()

    #list of boundaries used for collision detection
    #Maybe there should be a way of regulating the size of the list
    #like only include boundaries that are on the game display
    boundaryList = []
    boundaryList.append(floor)

    testBlock = Player(displayWidth/2,displayHeight/2,50,30,0,0,color = green)
    
    while running:

        testBlock.movement(boundaryList)
        testBlock.renderActor()

        clock.tick(15)
