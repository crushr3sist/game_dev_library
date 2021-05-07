import pygame


class draw_rectangle:
    def __init__(self, x , y, width, height):
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        

    
    def draw(self,screen,rectangle):
        self.color = (255,255,255)
        self.rectangle = rectangle
        rectangle = pygame.Rect(self.x, self.y, self.width, self.height)
        return_var = pygame.draw.rect(screen, self.color, rectangle)
        pygame.display.update(return_var)
        return return_var

