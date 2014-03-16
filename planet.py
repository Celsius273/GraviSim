import pygame, sys,os, time, random, platform, math
from pygame.locals import * 
from pygame.color import THECOLORS

#drawing functions
def image_get(folder, image):
    pygame.image.load(os.path.join(folder, image))
def text(text, font, color,x,y):
    text = font.render(text, True, (color[0],color[1],color[2]))
    screen.blit(text, (x,y))
def fill(color):
    screen.fill(THECOLORS[color])
def circle(color, x, y, radius):
    pygame.draw.circle(screen, color, (x, y), radius)
def flip():
    pygame.display.flip()
def blit(image, x, y):
    screen.blit(image, (x,y))
    
def round(x):
    if x-int(x) >= 0.5:
        return int(math.ceil(x))
    else:
        return int(math.floor(x))

class planet:
    def __init__ (self, p, v, r, d, i, cc=None):
        self.pos=[p[0], p[1]]
        self.velo=[v[0], v[1]]
        self.acc=[None, None]
        self.size=r
        self.density=d 
        self.mass=self.density*pow(r,3)
        if cc==None:
            
            self.color=[random.randint(0,255), random.randint(0,255), random.randint(0,255)]
        else:
            self.color=[cc[0],cc[1],cc[2]]
        self.id=i
        self.type="p"
    
    def setpos(self, x, y):
        self.pos[0]=x
        self.pos[1]=y
    
    def setvelo(self):
        self.velo[0]=self.velo[0]+self.acc[0]
        self.velo[1]=self.velo[1]+self.acc[1]
    
    def fvelo(self, xv, yv):
        self.velo[0]=xv
        self.velo[1]=yv
        
    def setacc(self, plist):
        if (len(plist)==0):
            self.acc=[0,0]
        else:
            self.acc=[0,0]
            for p in plist:
                if p.id != self.id: #applies to all objects without the same id
                    g=0.4 #10^-1... tweak this value as appropriate
                    
                    r=pow(pow(p.pos[1]-self.pos[1], 2) + pow(p.pos[0]-self.pos[0], 2) ,0.5)
                    if r <= 1: #lower limit for proportionality
                        r=1
                    mag = (g*p.density*pow(p.size, 3))/pow(r,2)
                    theta=math.atan2( p.pos[1]-self.pos[1], p.pos[0]-self.pos[0])
                    
                    self.acc[0]+= mag*math.cos(theta)
                    self.acc[1]+= mag*math.sin(theta)
                    
                    #GM/r^2
    
    def setrad(self, r): #can be useful later when eating up other planets
        self.size=r
    
    def move(self, plist): #this is moving per frame
        a=[0,1]
        for s in a:
            self.pos[s]+=self.velo[s]
        self.setacc(plist)
        self.setvelo()
        
    def gen(self, plist, idt): #will generate debris, a lot of this is just tinkering with constants
        
        ##Idea: define constants here and comment on what they're used for, will expedite process of tinkering
        
        for i in range (0, round(pow(self.size, 0.8))-1 ):
            plist.append( planet( [self.pos[0]+(random.randint(0,4*self.size)-2*self.size),self.pos[1]+(random.randint(0,4*self.size)-2*self.size)] , [ self.velo[0] + (-0.4+(0.8*random.random()))*self.velo[1] , self.velo[1] + (-0.4+(0.8*random.random()))*(-self.velo[0]) ], 1+random.randint(1, int(math.ceil(self.size/5.0))), self.density, idt+i+1))
        
    def setcolor(self):
        self.color[0]=random.randint(0,255)
        self.color[1]=random.randint(0,255)
        self.color[2]=random.randint(0,255)
        
    def draw(self):
        circle(self.color, round(self.pos[0]), round(self.pos[1]), self.size)
        
class star: #superheavy planets that won't move and have a LOT of mass
    def __init__ (self, p, r, d, i, cc=None):
        self.pos=[p[0], p[1]]
        self.velo=[0, 0]
        self.acc=[0, 0]
        self.size=r
        self.density=d 
        self.mass=self.density*pow(r,3)
        if cc==None:
            
            self.color=[random.randint(0,255), random.randint(0,255), random.randint(0,255)]
        else:
            self.color=[cc[0],cc[1],cc[2]]
        self.id=i
        self.type="s"
        
    def setpos(self, x, y):
        self.pos[0]=x
        self.pos[1]=y
        
    def setrad(self, r): #can be useful later when eating up other planets
        self.size=r
        
    def setcolor(self):
        self.color[0]=random.randint(0,255)
        self.color[1]=random.randint(0,255)
        self.color[2]=random.randint(0,255)
        
    def draw(self):
        circle(self.color, round(self.pos[0]), round(self.pos[1]), self.size)