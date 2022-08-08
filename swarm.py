from lib import *
from arena import Arena
from bot import Bot

class Swarm:
    def __init__(self, Arena: Arena, n, Bot: Bot):
        self.Arena = Arena
        self.n = n
        self.Bot = Bot
        self.botlist = self.generate(n)

    # Function used when animating bots.
    # Updates bots and redraws on given axis.
    def animate(self, t, ax):
        # ** Use this to update the bounds of the arena while animating ** #
        # if(t == 100):
        #     self.Arena.w *= 5
        #     self.Arena.h *= 5
        #     self.Arena.boundsup()
        ax.clear()
        ax.set_xlim(-self.Arena.dw, self.Arena.dw)
        ax.set_ylim(-self.Arena.dh, self.Arena.dh)
        self.update()
        self.draw(ax)
    
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
            bot.rotate(randbw(0.2, 100))

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
                self.botlist[i].collision(self.botlist[j])

    def draw(self, ax):
        for bot in self.botlist:
            bot.draw(ax)
        [ax.plot(bot.pos[0], bot.pos[1], 'bo') for bot in self.botlist]
        [ax.quiver(bot.pos[0], bot.pos[1], bot.uvec[0], bot.uvec[1], width = 0.003) for bot in self.botlist]

    # Generate and return a list of bots with positions
    # and directions having the specified resolutions
    def generate(self, n, p_res = 100, d_res = 100):
        return [self.Bot(self.Arena.w, self.Arena.h, p_res, d_res, 0.75, 1.5) for i in range(n)]