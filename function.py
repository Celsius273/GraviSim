import pygame, sys,os, time, random, platform, math

from pygame.locals import * 
from pygame.color import THECOLORS

def getImage(folder, image):
    pygame.image.load(os.path.join(folder, image))
    
def text(screen, x, y, text, color, font = None):
    if (font == None):
        font = pygame.font.Font("LUCON.TTF", 14)
    text = font.render(text, True, (color[0],color[1],color[2]))
    screen.blit(text, (x,y))

def fill(screen, color):
    screen.fill(THECOLORS[color])

def line(screen, x1, y1, x2, y2, color):
    pygame.draw.line(screen, color, (x1, y1), (x2, y2))

def circle(screen, x, y, radius, color):
    pygame.draw.circle(screen, color, ( round(x) , round(y) ), round(radius))

def rect(screen, x, y, length, width, color):
    pygame.draw.rect(screen, color, (x, y, length, width))

def flip():
    pygame.display.flip()

def drawImage(screen, x, y, image):
    screen.blit(image, (x,y))

def round(x):
    if x-int(x) >= 0.5:
        return int(math.ceil(x))
    else:
        return int(math.floor(x))

def dist(a,b,c,d):
    return pow( pow(c-a,2) + pow(d-b,2) , 0.5)    
    
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

class box:
    def __init__ (self, x, y, length, height = None):
        self.x = x
        self.y = y
        self.length = length
        if height == None:
            self.height = length
        else:
            self.height = height

    def setCoords(self, x, y):
        self.x = x
        self.y = y