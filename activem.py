from lib import *
from bot import Bot
from circlebot import CircleBot
from ellipsebot import EllipseBot
from swarm import Swarm
from arena import Arena

# Function used in FuncAnimation
def animate(t, swarm):
    ax.clear()
    ax.set_xlim(-arena.dw, arena.dw)
    ax.set_ylim(-arena.dh, arena.dh)
    swarm.update()
    [ax.plot(bot.pos[0], bot.pos[1], 'bo') for bot in swarm.botlist]
    [ax.quiver(bot.pos[0], bot.pos[1], bot.uvec[0], bot.uvec[1], width = 0.003) for bot in swarm.botlist]

""" Main Body """
save = False
numbots = 10
arena = Arena(5, 5)
swarm = Swarm(arena, numbots, CircleBot)

if(save):
    aniframes = 300
    fig = plt.figure(figsize = (12, 9))
    ax = fig.add_subplot(111, xlim = (-arena.dw, arena.dw), ylim = (-arena.dh, arena.dh))
    ani = FuncAnimation(fig, animate, fargs = (swarm,), interval = 10, frames = aniframes, repeat = False)
    ani.save("animation.mp4", fps = 30)
else:
    fig = plt.figure(figsize = (12, 9))
    ax = fig.add_subplot(111, xlim = (-arena.dw, arena.dw), ylim = (-arena.dh, arena.dh))
    ani = FuncAnimation(fig, animate, fargs = (swarm,), interval = 10, frames = None, repeat = False)
    plt.show()