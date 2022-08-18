import numpy as np
from matplotlib.patches import RegularPolygon

from ..fs import angfromuvec
from .bot import Bot

class TriBot(Bot):
    v = 0.08
    name = "TriBot"

    def __init__(self, upf, upfargs, r):
        self.r = r
        self.pos = np.array([0, 0])
        self.uvec = np.array([0, 1])
        self.normalizeuvec()
        self.upf = upf
        self.upfargs = upfargs

    def draw(self, ax):
        return ax.add_patch(RegularPolygon(self.pos, 3, self.r, angfromuvec(self.uvec) - np.pi/2, fill = False))

    def redraw(self, shape):
        shape.xy = self.pos
        shape.orientation = angfromuvec(self.uvec) - np.pi/2