from random import gauss

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from Lib.lib import randbw
from Lib.swarm import Swarm
from Lib.arenas import SqPerArena, SqReflArena, SqSolArena
from Lib.bots import CircleBot, EllipseBot, VicsekBot
from Lib.interaction import InteractionMethods as IM

""" Main Body """
dataout, animate, save = False, True, False
l, w, numbots = 5, 5, 10
arena = SqReflArena(l, w)
botlist = [CircleBot(gauss, (0, 0.2), 0.5) for _ in range(numbots)]
swarm = Swarm(arena, botlist, IM.ccollide)

if(save and animate):
    upframes = 300
    fig = plt.figure(figsize = (10, 9))
    ax = fig.add_subplot(111, xlim = (-swarm.Arena.dw, swarm.Arena.dw), ylim = (-swarm.Arena.dh, swarm.Arena.dh))
    ani = FuncAnimation(fig, swarm.animate, fargs = (ax,), interval = 10, frames = upframes, repeat = False)
    ani.save("animation.mp4", fps = 30)
elif(animate):
    fig = plt.figure(figsize = (10, 9))
    ax = fig.add_subplot(111, xlim = (-swarm.Arena.dw, swarm.Arena.dw), ylim = (-swarm.Arena.dh, swarm.Arena.dh))
    plot, quiver, shapes = swarm.ani_init(ax)
    ani = FuncAnimation(fig, swarm.animate, fargs = (ax, plot, quiver, shapes), interval = 50, frames = None, repeat = False)
    plt.show()
elif(dataout):
    frames = 2
    data = np.empty((numbots, frames))
    for i in range(frames):
        swarm.update()
        for j, bot in enumerate(swarm.botlist):
            print(f"{i}. {j + 1}: {bot.pos} {bot.uvec}")