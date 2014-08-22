import pygame, sys,os, time, random, platform, math, function
from function import *
from pygame.locals import * 
from pygame.color import THECOLORS

def round(x):
    if x-int(x) >= 0.5:
        return int(math.ceil(x))
    else:
        return int(math.floor(x))

def intersect(p1, p2, d): #self explanatory
    if p1[0]>=p2[0] and p1[0]<=p2[0]+d[0] and p1[1]>=p2[1] and p1[1]<=p2[1]+d[1]:
        return True
    else:
        return False
    
def dist(a,b,c,d):
    return pow( pow(c-a,2) + pow(d-b,2) , 0.5)

#class slider:   #slider object to control parameters, this will be hardcoded within the program itself as it's merely a part of the user interface so flexibility is not too big of a concern
    #def __init__ (self, p, l, h, sl, sh, lo, hi, i): #it might be a good idea to give fixed sizes for sliders, more on that after the image is designed
        #self.pos=[p[0],p[1]] #top left position of the slider
        #self.spos=[p[0],p[1]] #position for the selector
        #self.dim=[l,h] #length, height of the slider
        #self.sdim=[sl,sh]
        #self.low=lo #Low value
        #self.hi=hi #High value
        #self.id=i
        
        #self.val=(lo+hi)/2.0 #Initial value and appearance of slider to be set between low and high
                
        #self.select=False #again, self explanatory
        
        ##figure out how to do file paths in python, then load images for the bar and the selector for the slider
        ##as again, flexibility is not a concern as we're only using 3-4 sliders max
        
        ##self.bar=pygame.image.load()
        ##self.selector=pygame.image.load()
        
        ###Idea: learn the python image library and use it to automatically determine the image's dimensions
    
    ## Not sure how to really implement, so we're going to change the slider concept here
    #def sel(self, mpos, mb, slidelist):
        #if intersect(mpos, self.spos, self.sdim) == True and mb == (1,0,0):
            
            #osel=False #Are other sliders selected?
            ##Check another condition: only one slider can be selected at a time
            #for s in slidelist:
                #if s.sel(mpos, mb, slidelist)
            #self.select=True
        #if mb==(0,0,0):
            #self.select=False
            
    #def moveslider(self, mpos, mb): #The actual function that controls the value 
        #if self.select == True:
            ###dpos=[mpos[0]-self.spos[0],mpos[1]-self.spos[1]] 2d sliders maybe?
            ##So far, sliders would only need to be controlled in the x coordinates
            #dx=mpos[0]-self.spos[0]
            
            ##fill in here
    

class selector:
    def __init__ (self, pos, minValue, maxValue, increment, value, id, upButton, downButton):
        self.pos = pos
        self.minValue = minValue
        self.maxValue = maxValue
        self.increment = increment
        self.value = value
        self.id = id
        self.upButton = upButton
        self.downButton = downButton
        
    def draw(self, screen):
        
        return None
        
            
class button:
    def __init__ (self, pos, box, offImg, onImg):
        self.pos = pos
        self.box = box
        self.offImg = offImg
        self.onImg = onImg
        self.selected = False
    