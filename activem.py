from random import gauss

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from lib.fs import randbw
from lib.swarm import Swarm
import lib.arenas as arenas
import lib.bots as bots
from lib.interaction import InteractionMethods as IM

""" Main Body """
dataout, animate, save = False, True, False
l, w, numbots = 5, 5, 10
arena = arenas.SqPerArena(l, w)
botlist = [bots.EllipseBot(gauss, (0, 0.2), 1.5, 0.25) for _ in range(numbots)]
swarm = Swarm(arena, botlist, IM.ellcollide)

if(save and animate):
    upframes = 300
    ani_name = "animation.mp4"
    fig = plt.figure(figsize = (10, 9))
    ax = fig.add_subplot(111, xlim = (-swarm.Arena.dw, swarm.Arena.dw), ylim = (-swarm.Arena.dh, swarm.Arena.dh))
    plot, quiver, shapes = swarm.ani_init(ax)
    ani = FuncAnimation(fig, swarm.animate, fargs = (ax, plot, quiver, shapes), interval = 10, frames = upframes, repeat = False)
    ani.save(ani_name, fps = 20)

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