from lib import *
from swarm import Swarm
from circlebot import CircleBot
from ellipsebot import EllipseBot
from sqreflarena import SqReflArena

""" Main Body """
save = False
l, w, numbots = 5, 5, 10
swarm = Swarm(SqReflArena(l, w), numbots, EllipseBot, a = 0.25, b = 1.5)

if(save):
    aniframes = 300
    fig = plt.figure(figsize = (10, 9))
    ax = fig.add_subplot(111, xlim = (-swarm.Arena.dw, swarm.Arena.dw), ylim = (-swarm.Arena.dh, swarm.Arena.dh))
    ani = FuncAnimation(fig, swarm.animate, fargs = (ax,), interval = 10, frames = aniframes, repeat = False)
    ani.save("animation.mp4", fps = 30)
else:
    fig = plt.figure(figsize = (10, 9))
    ax = fig.add_subplot(111, xlim = (-swarm.Arena.dw, swarm.Arena.dw), ylim = (-swarm.Arena.dh, swarm.Arena.dh))
    ani = FuncAnimation(fig, swarm.animate, fargs = (ax,), interval = 10, frames = None, repeat = False)
    plt.show()