from lib import *
from arena import Arena
from bot import Bot

class Swarm:
    collrad = 0.3
    collang = np.pi

    def __init__(self, Arena: Arena, n, Bot: Bot):
        self.Arena = Arena
        self.n = n
        self.Bot = Bot
        self.botlist = self.generate(n)

    # This function is called on every frame of animation
    # to update the bots' angles, perform movement, and
    # check collisions
    def update(self):
        self.updateuvec()
        self.updatepos()
        self.docollisions()

    # Change the angle of the bot by a small random amount
    def updateuvec(self):
        for bot in self.botlist:
            bot.rotate(randbw(1, 100), randbw(0.1, 100))
            bot.rotatecart(randbw(0.1, 100), randbw(0.1, 100))

    # Step the bot forward one unit of its velocity
    # in the direction of its uvec
    def updatepos(self):
        for bot in self.botlist:
            bot.pos += bot.v*bot.uvec
            
            if(bot.pos[0] < -self.Arena.w):
                bot.pos[0] = -self.Arena.w
                bot.uvec[0] *= -1
            elif(bot.pos[0] > self.Arena.w):
                bot.pos[0] = self.Arena.w
                bot.uvec[0] *= -1
            if(bot.pos[1] < -self.Arena.h):
                bot.pos[1] = -self.Arena.h
                bot.uvec[1] *= -1
            elif(bot.pos[1] > self.Arena.h):
                bot.pos[1] = self.Arena.h
                bot.uvec[1] *= -1

    # Check whether each bot is in range of others
    # and is on a collision course. If so,
    # shift each of them away from each other by half
    # the distance required to get them out of collision
    # range
    def docollisions(self):
        for i in range(len(self.botlist)):
            for j in range(len(self.botlist)):
                if(i == j):
                    continue
                bota, botb = self.botlist[i], self.botlist[j]
                d = distance(bota.pos, botb.pos)
                if(d < self.collrad and angle(bota.uvec, vecdiffr(bota.pos, botb.pos, 1)) < self.collang and sees(bota.pos, bota.uvec, self.collang, botb.pos)[0]):
                    vec = vecdiffr(bota.pos, botb.pos, (self.collrad - d)/2)
                    botb.pos += vec
                    bota.pos -= vec

    # Generate and return a list of bots with positions
    # and directions having the specified resolutions
    def generate(self, n, p_res = 100, d_res = 100):
        W, H = self.Arena.w, self.Arena.h
        return [self.Bot([randbw(W, p_res), randbw(H, p_res)], [randbw(1, d_res), randbw(1, d_res)], self.Arena, self.Arena.w, self.Arena.h) for i in range(n)]