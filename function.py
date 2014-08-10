import pygame, sys,os, time, random, platform, math

from pygame.locals import * 
from pygame.color import THECOLORS

def round(x):
    if x-int(x) >= 0.5:
        return int(math.ceil(x))
    else:
        return int(math.floor(x))

def containsPoint(x, y, rect):
    xCheck = (x >= rect.x and x <= (rect.x+rect.length))
    yCheck = (y >= rect.y and y <= (rect.y+rect.height))
    
    if (xCheck and yCheck):
        return True
    return False
    
def intersectRect(rect1, rect2):
    xCheck = (rect1.x >= rect2.x and rect1.x <= (rect2.x + rect2.length)) or ((rect1.x+rect1.length) >= rect2.x and (rect1.x+rect1.length) <= (rect2.x + rect2.length))
    
    yCheck = (rect1.y >= rect2.y and rect1.y <= (rect2.y + rect2.height)) or ((rect1.y+rect1.height) >= rect2.y and (rect1.y+rect1.height) <= (rect2.y + rect2.height))
    
    if (xCheck and yCheck):
        return True
    return False

class Rect:
    def __init__ (x, y, length, height = None):
        self.x = x
        self.y = y
        self.length = length
        if height == None:
            self.height = length
        else:
            self.height = height