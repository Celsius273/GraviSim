import pygame, sys,os, time, random, platform, math, planet

from planet import planet, star
from pygame.locals import * 
from pygame.color import THECOLORS

## If you get the no available video device error, copy and paste the below code ##
if platform.system() == "Windows":
    os.environ['SDL_VIDEODRIVER'] = 'windib'
### If you get the no available video device error, copy and paste the above code ###

# This is the basic setup procedure
pygame.init() 
clock=pygame.time.Clock()
window = pygame.display.set_mode((800, 760)) 
pygame.display.set_caption('GravSim') 
screen = pygame.display.get_surface()
screen.fill(THECOLORS['black'])

test=pygame.display.get_driver()
#Setup ends

##Add functions, files and lists here

#fonts
f1 = pygame.font.Font("LUCON.TTF", 10)

#drawing functions
def image_get(folder, image):
    pygame.image.load(os.path.join(folder, image))
def text(text, font, color,x,y):
    text = font.render(text, True, (color[0],color[1],color[2]))
    screen.blit(text, (x,y))
def fill(color):
    screen.fill(THECOLORS[color])
def line(color, a, b, c, d,):
    pygame.draw.line(screen, color, (a, b), (c, d))
def circle(color, x, y, radius):
    pygame.draw.circle(screen, color, (x, y), radius)
def rect(color, a, b, c, d):
    pygame.draw.rect(screen, color, (a, b, c-a, d-b))
def flip():
    pygame.display.flip()
def blit(image, x, y):
    screen.blit(image, (x,y))
    
def round(x):
    if x-int(x) >= 0.5:
        return int(math.ceil(x))
    else:
        return int(math.floor(x))

def dist(a,b,c,d):
    return pow( pow(c-a,2) + pow(d-b,2) , 0.5)
    
tloop=0
running= True

plist=[] #list for all planets
tplist=[] #temporary list to store drag-eable planets

#testing 2 planets right now
plist.append(planet([400, 150] , [1.581988897,0] , 14, 0.04, 1))
plist.append(planet([300, 100] , [1.581988897,1] , 12, 0.07, 2))

plist.append(star([400, 300], 20, 0.2, 3, [255,160,0]))


#boolean 0/1 as for whether the user can add a planet or not when the mouse is pressed
add=1

# 1 for target, 2 for random, 3 for circle cw and 4 for circle ccw
addmode=1

rm=3 #random multiplier, you'll see what it does later =D

idt=4 #id tag, will increment by 1 every time a new object is added

hpos=[0,0] #if the mouse is dragged, this is the original drag point

try:
    while running:
        
        #Variables tracking the mouse and the keyboard
        mpos=pygame.mouse.get_pos()
        mb = pygame.mouse.get_pressed()
        
        if mb ==(1, 0, 0): #mouse press, right now, pressing anywhere will add a planet
            if add==1:
                add=0
                if addmode==2 :
                    plist.append(planet([mpos[0], mpos[1]] , [rm*(2*random.random()-1),rm*(2*random.random()-1)] , 10, 0.2, idt))
                if addmode==1:
                    tplist.append(planet([hpos[0], hpos[1]] , [rm*(2*random.random()-1),rm*(2*random.random()-1)] , 11, 0.2, idt,[0,0,255]))
            
            idt+=1
        if mb == (0,0,0): #mouse release/idle
            if len(tplist)>=1:
                tplist[0].fvelo((mpos[0]-hpos[0])/-50.0,(mpos[1]-hpos[1])/-50.0)
                #tplist[0].fvelo(5,5)
                plist.append(tplist[0])
                tplist.pop(0)
            hpos[0]=mpos[0]
            hpos[1]=mpos[1]
            if add ==0:
                add=1
            
        events=pygame.event.get()
        for e in events: 
            
            if e.type == QUIT:
                running=False   # Stop the program
                
        for p in plist:
            if p.type == "p":
                
                p.move(plist)
                
                for j in plist:   #checking for collision
                    if dist(p.pos[0],p.pos[1],j.pos[0],j.pos[1]) <= (p.size + j.size)and p.id != j.id:
                        if j.type=="s":
                            plist.remove(p)
                        elif j.type=="p":
                            if p.size >2 and j.size >2:
                                
                                p.gen(plist, idt)
                                idt+=round(pow(p.size, 0.8))-1
                                j.gen(plist, idt)
                                idt+=round(pow(j.size, 0.8))-1
                                p.setpos(random.randint(1000,4000),random.randint(1000,4000))
                                j.setpos(random.randint(1000,4000),random.randint(1000,4000)) #teleports the planets really far away, and they're then removed due to being out of bounds
        
                            
        for p in plist:
            if p.pos[0] > 800+p.size or p.pos[0] < 0-p.size or p.pos[1] > 600+p.size or p.pos[1] < 0-p.size:
                plist.remove(p)
                
        #anything under this line and above flip() is the drawing loop
        screen.fill(THECOLORS['black'])
        text(str(hpos[0]),f1, (0,255,255), 0, 0)
        text(str(hpos[1]),f1, (0,255,255), 0, 30)
        
        for p in plist:
            #p.draw()
            if p.size == 1:
                circle(p.color, round(p.pos[0]), round(p.pos[1]), 2)
            else:
                circle(p.color, round(p.pos[0]), round(p.pos[1]), round(p.size))
        
        for p in tplist:
            line((255,0,0),p.pos[0],p.pos[1],mpos[0],mpos[1])
            circle(p.color, round(p.pos[0]), round(p.pos[1]), p.size)
            
        rect( (55,55,55),0,600,800,760)
        flip()
        
                
        tloop+=1 #Every frame, the counter for the frames elapsed goes up by 1
        clock.tick(60) #60 fps
        
finally:
    pygame.quit()  # Keep this IDLE friendly 