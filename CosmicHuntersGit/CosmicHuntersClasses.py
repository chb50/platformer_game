import pygame
from CosmicHuntersProperties import *

#general class that most (if not all) objects in the game will
#inherit from
class Sprite(object):
    #to include this init within future classes that inherit from
    #this 1, use the "super" keyword
    def __init__(self, xCoord, yCoord, xSize,
                 ySize, xVel, yVel, color = None, img = None):
        #location of sprite
        self.xCoord = xCoord
        self.yCoord = yCoord
        #size of sprite
        self.xSize = xSize
        self.ySize = ySize
        #sprite hurt box
        self.xHurt = [xCoord, xCoord + xSize]
        self.yHurt = [yCoord, yCoord + ySize]
        #velocity of sprite
        self.xVel = xVel
        self.yVel = yVel
        #visual of object
        self.color = color
        self.img = img

    def getCoords(self):
        return self.xCoord, self.yCoord

    def getVel(self):
        return self.xVel, self.yVel

    def getSize(self):
        return self.xVel, self.yVel

    def getHurtBox(self):
        return self.xHurt, self.yHurt

    #used to alling the hurt box with any changes of position of sprite
##    def moveBox(self):
##        self.xHurt = [self.xCoord, self.xCoord + self.xSize]
##        self.yHurt = [self.yCoord, self.yCoord + self.ySize]

class Boundary(Sprite):
    def renderBoundary(self):
        pygame.draw.rect(gameDisplay, self.color,
                         (self.xCoord, self.yCoord, self.xSize, self.ySize))
        pygame.display.update()

#class used for enemies, player character
class Actor(Sprite):
    #this function is used for collision detection with walls
    def movement(self, boundary):
        return

    def renderActor(self):
        pygame.draw.rect(gameDisplay, self.color,
                         (self.xCoord, self.yCoord, self.xSize, self.ySize))
        pygame.display.update()

class Player(Actor):
    def movement(self, boundaryList):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.xVel = -10
                    #boundaries to left of player
                    for boundary in boundaryList:
                        if self.xHurt[0] + self.xVel < boundary.xHurt[1] and self.xHurt[0] + self.xVel > boundary.xHurt[0] and self.yHurt[1] > boundary.yHurt[0] and self.yHurt[0] < boundary.yHurt[1]:
                            self.xVel = 0
                            
                if event.key == pygame.K_d:
                    self.xVel = 10
                    #boundaries to right of player
                    for boundary in boundaryList:
                        if self.xHurt[1] + self.xVel > boundary.xHurt[0] and self.xHurt[1] + self.xVel < boundary.xHurt[1] and self.yHurt[1] > boundary.yHurt[0] and self.yHurt[0] < boundary.yHurt[1]:
                            self.xVel = 0
                            
                #this will change when projectile motion is implemented
                #just testing for boundary collision for now
                if event.key == pygame.K_w:
                    self.yVel = -10
                    for boundary in boundaryList:
                        if self.yHurt[0] + self.yVel < boundary.yHurt[1] and self.yHurt[0] + self.yVel > boundary.yHurt[0] and self.xHurt[1] > boundary.xHurt[0] and self.xHurt[0] < boundary.xHurt[1]:
                            self.yVel = 0
                            
                if event.key == pygame.K_s:
                    self.yVel = 10
                    for boundary in boundaryList:
                        if self.yHurt[1] + self.yVel > boundary.yHurt[0] and self.yHurt[1] + self.yVel < boundary.yHurt[1] and self.xHurt[1] > boundary.xHurt[0] and self.xHurt[0] < boundary.xHurt[1]:
                            self.yVel = 0
                            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    self.xVel = 0
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    self.yVel = 0

        #update coordinate with velocity
        self.xCoord += self.xVel
        self.yCoord += self.yVel

        #update hurt box with new coordinates
        self.xHurt = [self.xCoord, self.xCoord + self.xSize]
        self.yHurt = [self.yCoord, self.yCoord + self.ySize]

#TODO:
#colision detection - can move through floor if button is held down while making contact with floor
