import pygame, sys,os, time, random, platform, math, function
from function import *
from pygame.locals import * 
from pygame.color import THECOLORS

class selector:
    def __init__ (self, pos, minValue, maxValue, increment, id, title, upButton, downButton):
        self.pos = pos
        self.minValue = minValue
        self.maxValue = maxValue
        self.increment = increment
        self.value = (minValue + maxValue)/2
        self.id = id
        self.title = title
        self.upButton = upButton
        self.downButton = downButton

        self.downButton.setCoords(self.pos[0] - 22, self.pos[1] + 20)
        self.upButton.setCoords(self.pos[0] + 88, self.pos[1] + 20)
        
    def draw(self, screen):
        text(screen, self.pos[0], self.pos[1], self.title, [222,222,222])
        text(screen, self.pos[0], self.pos[1]+20, "value: "+str(self.value), [222,222,222])

        self.upButton.draw(screen)
        self.downButton.draw(screen)

        return None

    def getButtonPressed(self, mpos):
        # mpos is a 2-tuple of the mouse's position on the screen
        if function.containsPoint(mpos[0], mpos[1], self.downButton.box):
            return -1
        elif function.containsPoint(mpos[0], mpos[1], self.upButton.box):
            return 1
        else:
            return 0
            
class button:
    def __init__ (self, box, onImg, offImg):
        self.box = box #box is of a function.Rect type
        self.onImgString = onImg # image filenames
        self.offImgString = offImg

        # converting specified image filenames into pygame surfaces
        self.offImg = pygame.image.load(offImg).convert()
        self.onImg = pygame.image.load(onImg).convert()
        # scaling the graphic to the size of the button's hitbox (which is a rectangle)
        self.offImg = pygame.transform.scale(self.offImg, (self.box.length, self.box.height))
        self.onImg = pygame.transform.scale(self.onImg, (self.box.length, self.box.height))

        self.selected = False
    def draw(self, screen):
        if (self.selected):
            function.drawImage(screen, self.box.x, self.box.y, self.onImg)
        else:
            function.drawImage(screen, self.box.x, self.box.y, self.offImg)
        #function.rect(screen, box.x, box.y, box.length, box.width)

    def setCoords(self, x, y):
        self.box.setCoords(x, y)

