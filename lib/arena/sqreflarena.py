from .arena import Arena
from numpy import array
from ..fs import randbw

class SqReflArena(Arena):
    def __init__(self, h: float, w: float):
        self.boundschanged = False
        self.h = h
        self.w = w
        self.boundsup()

    # Update the variables used for plot bounds if/when the
    # arena bounds are changed
    def boundsup(self):
        self.dh, self.dw = self.h + self.h/10, self.w + self.w/10
        self.boundschanged = True

    def boundcoll(self, items: list):
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

    def randpos(self, bot):
        bot.pos = array([randbw(self.w), randbw(self.h)])