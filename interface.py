class slider:   #slider object to control parameters, this will be hardcoded within the program itself as it's merely a part of the user interface so flexibility is not too big of a concern
    def __init__ (self, p, l, h, lo, hi, i): #it might be a good idea to give fixed sizes for sliders, more on that after the image is designed
        self.pos=[p[0],p[1]]
        self.spos=[p[0],p[1]] #position for the selector
        self.length=l
        self.height=h
        self.low=lo
        self.hi=hi
        self.id=i
        
        self.val=low
                
        #figure out how to do file paths in python, then load images for the bar and the selector for the slider
        #as again, flexibility is not a concern as we're only using 3-4 sliders max
        
        #self.bar=pygame.image.load()
        #self.selector=pygame.image.load()
        
        ##Idea: learn the python image library and use it to automatically determine the image's dimensions
    

class button:
    