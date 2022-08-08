from lib import *
from bot import Bot
from circlebot import CircleBot
from ellipsebot import EllipseBot
from swarm import Swarm
from arena import Arena

""" Main Body """
save = False
l, w, numbots = 5, 5, 10
swarm = Swarm(Arena(l, w), numbots, EllipseBot)

if(save):
    aniframes = 300
    fig = plt.figure(figsize = (12, 9))
    ax = fig.add_subplot(111, xlim = (-swarm.Arena.dw, swarm.Arena.dw), ylim = (-swarm.Arena.dh, swarm.Arena.dh))
    ani = FuncAnimation(fig, swarm.animate, fargs = (ax,), interval = 10, frames = aniframes, repeat = False)
    ani.save("animation.mp4", fps = 30)
else:
    fig = plt.figure(figsize = (12, 9))
    ax = fig.add_subplot(111, xlim = (-swarm.Arena.dw, swarm.Arena.dw), ylim = (-swarm.Arena.dh, swarm.Arena.dh))
    ani = FuncAnimation(fig, swarm.animate, fargs = (ax,), interval = 10, frames = None, repeat = False)
    plt.show()