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
        self.Arena.boundcoll(self.botlist)
        self.collf(self.botlist)

    # Change the angle of the bot by a small random amount
    def updateuvec(self):
        for bot in self.botlist:
            bot.rotate(bot.upf(*bot.upfargs))

    # Step the bot forward one unit of its velocity
    # in the direction of its uvec
    def updatepos(self):
        for bot in self.botlist: bot.pos += bot.v*bot.uvec

    def draw(self, ax):
        for bot in self.botlist:
            bot.draw(ax)
        for bot in self.botlist: ax.plot(bot.pos[0], bot.pos[1], 'bo')
        for bot in self.botlist: ax.quiver(bot.pos[0], bot.pos[1], bot.uvec[0], bot.uvec[1], width = 0.003)