from lib import *

# Class for the arena in which the bots are interacting.
# Mainly just a container for x and y bounds
class Arena:
    def __init__(self, h, w):
        self.h = h
        self.w = w
        self.boundsup()

    # TODO: Boundary types:
    # TODO - Periodic
    # TODO - Solid
    # DONE - Reflective

    # Update the variables used for plot bounds if/when the
    # arena bounds are changed
    def boundsup(self):
        self.dh, self.dw = self.h + self.h/10, self.w + self.w/10

    def boundcoll(self, items):
        for item in items:            
            if(item.pos[0] < -self.w):
                item.pos[0] = -self.w
                item.uvec[0] *= -1
            elif(item.pos[0] > self.w):
                item.pos[0] = self.w
                item.uvec[0] *= -1
            if(item.pos[1] < -self.h):
                item.pos[1] = -self.h
                item.uvec[1] *= -1
            elif(item.pos[1] > self.h):
                item.pos[1] = self.h
                item.uvec[1] *= -1