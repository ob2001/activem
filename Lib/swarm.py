import random

from .fs import np

class Swarm:
    def __init__(self, arena, botlist, collf):
        self.Arena = arena
        self.botlist = botlist
        self.collf = collf

        for bot in self.botlist:
            bot.randpos(self.Arena.h, self.Arena.w)
            bot.randuvec()

    def set_collider(self, collf):
        self.collf = collf

    def regenerate(self, upf, upfargs, **kwargs):
        self.botlist = [self.Bot(self.Arena.w, self.Arena.h, upf, upfargs, **kwargs)]

    def ani_init(self, ax):
        xs, ys, dxs, dys = [bot.pos[0] for bot in self.botlist], [bot.pos[1] for bot in self.botlist], [bot.uvec[0] for bot in self.botlist], [bot.uvec[1] for bot in self.botlist]
        plot, = ax.plot(xs, ys, 'bo')
        quiver = ax.quiver(xs, ys, dxs, dys, width = 0.003)
        shapes = [bot.draw(ax) for bot in self.botlist]
        return plot, quiver, shapes

    # Function used when animating bots.
    # Updates bots and redraws on given axis.
    def animate(self, t, ax, plots, quivers, shapes):
        # ** Use this to update the bounds of the arena while animating ** #
        # if(t == 100):
        #     self.Arena.w *= 5
        #     self.Arena.h *= 5
        #     self.Arena.boundsup()
        if(self.Arena.boundschanged):
            ax.set_xlim(-self.Arena.dw, self.Arena.dw)
            ax.set_ylim(-self.Arena.dh, self.Arena.dh)
            self.Arena.boundschanged = False
        self.update()
        self.draw(plots, quivers, shapes)
    
    # This function is called on every frame of animation
    # to update the bots' angles, perform movement, and
    # check collisions
    def update(self):
        # Change the angle of the bot by a small random amount
        [bot.rotate(bot.upf(*bot.upfargs)) for bot in self.botlist]
        
        # Step the bot forward one unit of its velocity
        # in the direction of its uvec
        for bot in self.botlist: bot.pos += bot.v*bot.uvec
        
        self.Arena.boundcoll(self.botlist)
        self.collf(random.sample(self.botlist, len(self.botlist)))

    def draw(self, plot, quiver, shapes):
        xs, ys, dxs, dys = [bot.pos[0] for bot in self.botlist], [bot.pos[1] for bot in self.botlist], [bot.uvec[0] for bot in self.botlist], [bot.uvec[1] for bot in self.botlist]
        for i, bot in enumerate(self.botlist):
            plot.set_data(xs, ys)
            quiver.set_offsets(np.c_[xs, ys])
            quiver.set_UVC(dxs, dys)
            bot.redraw(shapes[i])
