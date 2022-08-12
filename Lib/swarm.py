from .lib import *
from Lib.Bot.bot import Bot
from Lib.Arena.arena import Arena

class Swarm:
    def __init__(self, Arena: Arena, n, Bot: Bot, **kwargs):
        self.Arena = Arena
        self.n = n
        self.Bot = Bot

        # Generate and return a list of bots with positions
        # and directions having the specified resolutions
        self.botlist = [self.Bot(self.Arena.w, self.Arena.h, kwargs) for _ in range(n)]

    # Function used when animating bots.
    # Updates bots and redraws on given axis.
    def animate(self, t, ax, func, *args):
        # ** Use this to update the bounds of the arena while animating ** #
        # if(t == 100):
        #     self.Arena.w *= 5
        #     self.Arena.h *= 5
        #     self.Arena.boundsup()
        ax.clear()
        ax.set_xlim(-self.Arena.dw, self.Arena.dw)
        ax.set_ylim(-self.Arena.dh, self.Arena.dh)
        self.update(func, args)
        self.draw(ax)
    
    # This function is called on every frame of animation
    # to update the bots' angles, perform movement, and
    # check collisions
    def update(self, func, args):
        self.updateuvec(func, args)
        self.updatepos()
        self.docollisions()

    # Change the angle of the bot by a small random amount
    def updateuvec(self, func, args):
        for bot in self.botlist:
            bot.rotatef(func, args)

    # Step the bot forward one unit of its velocity
    # in the direction of its uvec
    def updatepos(self):
        for bot in self.botlist: bot.pos += bot.v*bot.uvec

    # Check whether each bot is in range of others
    # and is on a collision course. If so,
    # shift each of them away from each other by half
    # the distance required to get them out of collision
    # range
    def docollisions(self):
        self.Arena.boundcoll(self.botlist)
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