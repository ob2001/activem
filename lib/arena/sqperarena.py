from .arena import Arena
from ..fs import randbw
from numpy import array

class SqPerArena(Arena):
    def __init__(self, h: float, w: float):
        self.h = h
        self.w = w
        self.boundschanged = False
        self.boundsup()

    def boundsup(self):
        self.dh, self.dw = self.h + self.h/10, self.w + self.w/10
        self.boundschanged = True

    def boundcoll(self, items: list):
        for item in items:            
            if(item.pos[0] < -self.w): item.pos[0] += 2*self.w
            elif(item.pos[0] > self.w): item.pos[0] -= 2*self.w
            if(item.pos[1] < -self.h): item.pos[1] += 2*self.h
            elif(item.pos[1] > self.h): item.pos[1] -= 2*self.h

    def randpos(self, bot):
        bot.pos = array([randbw(self.w), randbw(self.h)])