from typing import Callable
import numpy as np
from matplotlib.pyplot import Axes
from matplotlib.patches import Patch, Polygon

from ..fs import angfromuvec
from .bot import Bot

class TriBot(Bot):
    v = 0.08
    name = "TriBot"

    def __init__(self, upf: Callable, upfargs: tuple, r: float):
        self.r = r
        self.pos = np.array([0, 0])
        self.uvec = np.array([0, 1])
        self.normalizeuvec()
        self.upf = upf
        self.upfargs = upfargs
        self.colliding = False
        self.vertices = [[-0.1, 0], [0, 0.5], [0.1, 0], [0, -0.5]]

    def draw(self, ax: Axes) -> Patch:
        ang = angfromuvec(self.uvec)
        rotmat = np.array([[np.cos(ang), np.sin(ang)], [-np.sin(ang), np.cos(ang)]])
        return ax.add_patch(Polygon(self.vertices@rotmat + self.pos, closed = True, fill = False))

    def redraw(self, shape: Patch):
        ang = angfromuvec(self.uvec) - np.pi/2
        rotmat = np.array([[np.cos(ang), np.sin(ang)], [-np.sin(ang), np.cos(ang)]])
        shape.xy = self.vertices@rotmat + self.pos
        if self.colliding:
            shape.set_edgecolor('r')
            self.colliding = False
        else:
            shape.set_edgecolor('k')