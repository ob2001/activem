from lib import *

class Swarm:
    collrad = 1
    elastic = 0.02

    def __init__(self, Arena, n, Bot):
        self.Arena = Arena
        self.n = n
        self.Bot = Bot
        self.botlist = self.generate(n)

    # This function is called on every frame of animation
    # to update the bots' angles, perform movement, and
    # check collisions
    def update(self):
        # self.updateang()
        self.updatepos()
        self.docollisions()

    # Change the angle of the bot by a small random amount
    def updateang(self):
        for bot in self.botlist:
            bot.rotate(randbw(1, 100), randbw(0.1, 100))
            # bot.rotatecart(randbw(0.1, 100), randbw(0.1, 100))

    # Step the bot forward on unit of its velocity
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

    # Check whether each bot is in range of others.
    # If so, [do something that deflects them]
    def docollisions(self):
        for i in range(len(self.botlist)):
            for j in range(i + 1, len(self.botlist)):
                bota, botb = self.botlist[i], self.botlist[j]
                d = distance(bota.pos, botb.pos)
                if(d < self.collrad):
                    bota.rotate(1, np.pi)
                    botb.rotate(-1, np.pi)

    # Generate and return a list of bots with positions
    # and directions having the specified resolutions
    def generate(self, n, p_res = 100, d_res = 100):
        W, H = self.Arena.w, self.Arena.h
        return [self.Bot([randbw(W, p_res), randbw(H, p_res)], [randbw(1, d_res), randbw(1, d_res)], self.Arena, self.Arena.w, self.Arena.h) for i in range(n)]