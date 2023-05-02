from random import gauss
import time

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
arena = arenas.CirSolArena(2.5)
botlist = [bots.TriBot(gauss, (0, 0.1), 0.1) for _ in range(numbots)]
swarm = Swarm(arena, botlist, IM.ccollide)

if(save and animate):
    frames = 300
    ani_name = "animation.mp4"
    fig = plt.figure(figsize = (10, 9))
    ax = fig.add_subplot(111, xlim = (-swarm.Arena.dw, swarm.Arena.dw), ylim = (-swarm.Arena.dh, swarm.Arena.dh))
    aniargs = swarm.ani_init(ax)
    start = time.time()
    ani = FuncAnimation(fig, swarm.animate, fargs = (ax, *aniargs), interval = 10, frames = frames, repeat = False)
    ani.save(ani_name, fps = 20)
    print(f"Elapsed time for {frames} frames: {time.time() - start}")

elif(animate):
    fig = plt.figure(figsize = (10, 9))
    ax = fig.add_subplot(111, xlim = (-swarm.Arena.dw, swarm.Arena.dw), ylim = (-swarm.Arena.dh, swarm.Arena.dh))
    plot, quiver, shapes = swarm.ani_init(ax)
    ani = FuncAnimation(fig, swarm.animate, fargs = (ax, plot, quiver, shapes), interval = 50, frames = None, repeat = False)
    plt.show()

elif(dataout):
    frames = 300
    data = np.empty((numbots, frames))
    start = time.time()
    for i in range(frames):
        swarm.update()
        # for j, bot in enumerate(swarm.botlist):
            # print(f"{i}. {j + 1}: {bot.pos} {bot.uvec}")
    print(f"Elapsed time for {frames} frames: {time.time() - start}")