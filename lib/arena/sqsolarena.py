from ..fs import np
from .arena import Arena

class SqSolArena(Arena):
    def __init__(self, h: float, w: float):
        self.boundschanged = False
        self.h = h
        self.w = w
        self.boundsup()

    def boundsup(self):
        self.dh, self.dw = self.h + self.h/10, self.w + self.w/10
        self.boundschanged = True


    def boundcoll(self, items: list):
        for item in items:            
            if(item.pos[0] < -self.w): item.pos[0] = -self.w
            elif(item.pos[0] > self.w): item.pos[0] = self.w
            if(item.pos[1] < -self.h): item.pos[1] = -self.h
            elif(item.pos[1] > self.h): item.pos[1] = self.h