from .interaction import InteractionMethods as IM

from .fs import np

class Swarm:
    def __init__(self, arena, botlist, collf):
        self.Arena = arena
        self.botlist = botlist
        self.collf = collf

        for bot in self.botlist:
            bot.randpos(self.Arena.h, self.Arena.w)
            bot.randuvec()

    # Update collider being used at an arbitrary time during execution
    def set_collider(self, collf):
        self.collf = collf

    # Generate a new botlist composed of the same number and type of bots
    # used previously
    def regenerate(self, upf, upfargs, **kwargs):
        self.botlist = [self.Bot(self.Arena.w, self.Arena.h, upf, upfargs, **kwargs)]

    # Call before beginning animation to get artists used universally
    def ani_init(self, ax):
        xs, ys, dxs, dys = [bot.pos[0] for bot in self.botlist], [bot.pos[1] for bot in self.botlist], [bot.uvec[0] for bot in self.botlist], [bot.uvec[1] for bot in self.botlist]
        plot, = ax.plot(xs, ys, 'bo')
        quiver = ax.quiver(xs, ys, dxs, dys, width = 0.003)
        shapes = [bot.draw(ax) for bot in self.botlist]
        return plot, quiver, shapes

    # Function used when animating bots.
    # Updates bots and updates relevant plot elements
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

    # Updates the swarm by one timestep.
    # Handles motion and calls collision methods
    def update(self):
        # Change the angle of the bot by a small random amount
        for bot in self.botlist: bot.rotate(bot.upf(*bot.upfargs))
        
        # Step the bot forward one unit of its velocity
        # in the direction of its uvec
        for bot in self.botlist: bot.pos += bot.v*bot.uvec
        
        self.Arena.boundcoll(self.botlist)
        # print(IM.getccollisions(self.botlist))
        self.collf(self.botlist)

    # Called by animate function to redraw all plot elements
    def draw(self, plot, quiver, shapes):
        xs, ys, dxs, dys = [bot.pos[0] for bot in self.botlist], [bot.pos[1] for bot in self.botlist], [bot.uvec[0] for bot in self.botlist], [bot.uvec[1] for bot in self.botlist]
        for i, bot in enumerate(self.botlist):
            plot.set_data(xs, ys)
            quiver.set_offsets(np.c_[xs, ys])
            quiver.set_UVC(dxs, dys)
            bot.redraw(shapes[i])
