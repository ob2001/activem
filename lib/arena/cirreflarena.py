from .arena import Arena
from numpy import sqrt, array, pi, cos, sin
from ..fs import vecdiffn, randbw

class CirReflArena(Arena):
    def __init__(self, r: float):
        self.r = r
        self.boundschanged = False
        self.boundsup()

    def boundsup(self):
        self.dw = self.dh = self.r + 0.1*self.r
        self.boundschanged = True

    def boundcoll(self, items: list):
        for item in items:
            rpos = sqrt(item.pos[0]**2 + item.pos[1]**2)
            if(rpos > self.r):
                item.pos -= (rpos - self.r)*vecdiffn([0, 0], item.pos)

    def randpos(self, bot):
        bot.pos = randbw(0, self.r)*array([cos(randbw(0, 2*pi)), sin(randbw(0, 2*pi))])