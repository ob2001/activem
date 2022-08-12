from random import gauss

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from Lib.swarm import Swarm

from Lib.Bot.circlebot import CircleBot
from Lib.Bot.ellipsebot import EllipseBot
from Lib.Bot.vicsekbot import VicsekBot

from Lib.Arena.sqreflarena import SqReflArena
from Lib.Arena.sqperarena import SqPerArena
from Lib.Arena.sqsolarena import SqSolArena

""" Main Body """
dataout, animate, save = False, True, False
l, w, numbots = 5, 5, 10
swarm = Swarm(SqPerArena(l, w), numbots, VicsekBot, gauss, (0, 0.2), a = 0.25, b = 1.5)

if(save and animate):
    upframes = 300
    fig = plt.figure(figsize = (10, 9))
    ax = fig.add_subplot(111, xlim = (-swarm.Arena.dw, swarm.Arena.dw), ylim = (-swarm.Arena.dh, swarm.Arena.dh))
    ani = FuncAnimation(fig, swarm.animate, fargs = (ax,), interval = 10, frames = upframes, repeat = False)
    ani.save("animation.mp4", fps = 30)
elif(animate):
    fig = plt.figure(figsize = (10, 9))
    ax = fig.add_subplot(111, xlim = (-swarm.Arena.dw, swarm.Arena.dw), ylim = (-swarm.Arena.dh, swarm.Arena.dh))
    ani = FuncAnimation(fig, swarm.animate, fargs = (ax,), interval = 10, frames = None, repeat = False)
    plt.show()
elif(dataout):
    frames = 2
    data = np.empty((numbots, frames))
    for i in range(frames):
        swarm.update()
        for j, bot in enumerate(swarm.botlist):
            print(f"{i}. {j + 1}: {bot.pos} {bot.uvec}")