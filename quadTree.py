import pygame, sys,os, time, random, platform, math, planet, function

from planet import *
from function import *
from pygame.locals import * 
from pygame.color import THECOLORS



            
class quadTree:
    
    MAX_LEVELS = 7 #Static variables/parameters
    MAX_OBJECTS = 20    
    
    def __init__ (rect, level):
        self.rect=rect
        self.objects=[] #List of entities within the quadtree, we will have one type of quadtree per "relevant" object type
        self.level = level

        self.nodes = [] #List of contained quadtrees
        
        
        
    def getRect():
        return self.rect