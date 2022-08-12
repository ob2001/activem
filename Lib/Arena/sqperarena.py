from .arena import Arena

class SqPerArena(Arena):
    def __init__(self, h, w):
        self.h = h
        self.w = w
        self.boundsup()

    def boundsup(self):
        self.dh, self.dw = self.h + self.h/10, self.w + self.w/10

    def boundcoll(self, items):
        for item in items:            
            if(item.pos[0] < -self.w): item.pos[0] += 2*self.w
            elif(item.pos[0] > self.w): item.pos[0] -= 2*self.w
            if(item.pos[1] < -self.h): item.pos[1] += 2*self.h
            elif(item.pos[1] > self.h): item.pos[1] -= 2*self.h