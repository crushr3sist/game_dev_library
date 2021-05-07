from .initialise import *

class MainLoop():
    def __init__(self,width,height,title,runtype):
        self.width = width
        self.height = height
        self.resolution = (self.width, self.height)
        self.title = str(title)
        self.runtype = runtype
        if self.runtype == "debug":
            initialise(set_print=True)
        elif self.runtype == "std":
            initialise(set_print=False)

        
    def window(self):
        global screen
        pygame.display.init()
        screen = pygame.display.set_mode([self.width, self.height])
        screen.fill((0,0,0))
        return screen


    def check_for_events(self):
        Running = True 
        while Running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    Running = False 
                initialise()
                pygame.event.pump()





