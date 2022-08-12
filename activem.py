from random import gauss

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from Lib.lib import randbw
from Lib.swarm import Swarm
from Lib.Bot.circlebot import CircleBot
from Lib.Bot.ellipsebot import EllipseBot
from Lib.Arena.sqreflarena import SqReflArena

""" Main Body """
dataout, animate, save = False, True, False
l, w, numbots = 5, 5, 10
swarm = Swarm(SqReflArena(l, w), numbots, CircleBot, a = 0.25, b = 1.5)
anif, anifargs = randbw, (0.2,)

if(save and animate):
    aniframes = 300
    fig = plt.figure(figsize = (10, 9))
    ax = fig.add_subplot(111, xlim = (-swarm.Arena.dw, swarm.Arena.dw), ylim = (-swarm.Arena.dh, swarm.Arena.dh))
    ani = FuncAnimation(fig, swarm.animate, fargs = (ax,), interval = 10, frames = aniframes, repeat = False)
    ani.save("animation.mp4", fps = 30)
elif(animate):
    fig = plt.figure(figsize = (10, 9))
    ax = fig.add_subplot(111, xlim = (-swarm.Arena.dw, swarm.Arena.dw), ylim = (-swarm.Arena.dh, swarm.Arena.dh))
    ani = FuncAnimation(fig, swarm.animate, fargs = (ax, anif, *anifargs), interval = 10, frames = None, repeat = False)
    plt.show()
elif(dataout):
    pass