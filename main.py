import pygame, sys,os, time, random, platform, math, planet, interface, quadTree, function

from planet import *
from pygame.locals import * 
from interface import *
from quadTree import *
from function import *
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
    
tloop=0
running= True

plist=[] #list for all planets
tplist=[] #temporary list to store drag-eable planets

#testing 2 planets right now
plist.append(planet([400, 150] , [1.581988897,0] , 14, 0.04, 1))
plist.append(planet([300, 100] , [1.581988897,1] , 1, 0.07, 2))

plist.append(star([400, 300], 20, 0.2, 3, [255,160,0]))

#static variables
PLUS =pygame.image.load('plus.png')
MINUS =pygame.image.load('minus.png')
RED = (255,0,0)

#boolean 0/1 as for whether the user can add a planet or not when the mouse is pressed
add=1
select = 1

# 1 for target, 2 for random, 3 for circle cw and 4 for circle ccw
addmode=1

rm=3 #random multiplier, you'll see what it does later =D
idt=4 #id tag, will increment by 1 every time a new object is added
hpos=[0,0] #if the mouse is dragged, this is the original drag point

#setting up selectors for adjusting values
selectorList = []

sizeSel = selector( [300,700], 2, 14, 3, 0, "planet size",
button( box(0,0,16,16), "plusON.png", "plus.png") , button( box(0,0,16,16), "minusON.png","minus.png" ))

selectorList.append(sizeSel)
planet_size = 8
try:
    while running:
        #drawing, then mouse/keyboard input events, then dealing with objects currently on the screen

        #anything under this line and above flip() is the drawing loop
        screen.fill(THECOLORS['black'])
        #debug text
        function.text(screen, 0,0, str(hpos[0]), (0,255,255), f1)
        function.text(screen, 0,30, str(hpos[1]), (0,255,255), f1)

        #Variables tracking the mouse and the keyboard
        mpos=pygame.mouse.get_pos()
        mb = pygame.mouse.get_pressed()
        if mb ==(1, 0, 0): #mouse press, right now, pressing anywhere except for the bottom rectangle where the selectors/buttons are will add a planet

            for selector in selectorList:
                if (selector.getButtonPressed(mpos) == 1):
                    selector.upButton.selected = True
                    if selector.value + selector.increment <= selector.maxValue and select == 1:
                        selector.value += selector.increment
                elif (selector.getButtonPressed(mpos) == -1):
                    selector.downButton.selected = True
                    if selector.value - selector.increment >= selector.minValue and select == 1:
                        selector.value -= selector.increment

                if selector.id == 0:
                    planet_size = selector.value

            select = 0
            if (add == 1 and mpos[1] < 600):
                add=0
                if addmode==2 :
                    plist.append( planet([mpos[0], mpos[1]]
                    , [rm*(2*random.random()-1),rm*(2*random.random()-1)]
                    , planet_size, 0.2, idt))
                elif addmode==1:
                    tplist.append(planet([hpos[0], hpos[1]]
                    , [rm*(2*random.random()-1),rm*(2*random.random()-1)]
                    , planet_size, 0.2, idt))
                    #tplist.append(planet([hpos[0], hpos[1]], [rm*(2*random.random()-1),rm*(2*random.random()-1)] , 11, 0.2, idt,[0,0,255]))
            idt+=1
        elif mb == (0,0,0): #mouse release/idle
            if len(tplist)>=1:
                tplist[0].fvelo( (mpos[0]-hpos[0])/-100.0,(mpos[1]-hpos[1])/-100.0 )
                plist.append(tplist[0])
                tplist.pop(0)
            hpos[0]=mpos[0]
            hpos[1]=mpos[1]
            add=1
            select =1
            for selector in selectorList:
                selector.downButton.selected = False
                selector.upButton.selected = False
            
        events=pygame.event.get()
        for e in events:
            if e.type == QUIT:
                running=False   # Stop the program
                
        for p in plist:
            p.draw(screen)
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

            if p.pos[0] > 800+p.size or p.pos[0] < 0-p.size or p.pos[1] > 600+p.size or p.pos[1] < 0-p.size:
                plist.remove(p)

        for p in tplist:
            function.line(screen, p.pos[0],p.pos[1], mpos[0],mpos[1], RED)
            function.circle(screen, p.pos[0], p.pos[1], p.size,  p.color)
            
        function.rect(screen, 0,600, 800,160,  (55,55,55))
        for selector in selectorList:
            selector.draw(screen)
        function.flip()
        
                
        tloop+=1 #Every frame, the counter for the frames elapsed goes up by 1
        clock.tick(120) #120 fps
        
finally:
    pygame.quit()  # Keep this IDLE friendly 