from matplotlib.patches import RegularPolygon
from numpy import pi

from ..fs import angfromuvec
from .bot import Bot

class TriBot(Bot):
    v = 0.08
    name = "TriBot"

    def __init__(self, upf, upfargs, r):
        self.r = r
        self.pos = [0, 0]
        self.uvec = [0, 1]
        self.normalizeuvec()
        self.upf = upf
        self.upfargs = upfargs

    def draw(self, ax):
        return ax.add_patch(RegularPolygon((self.pos[0], self.pos[1]), 3, self.r, angfromuvec(self.uvec) - pi/2, fill = False))

    def redraw(self, shape):
        shape.xy = self.pos[0], self.pos[1]
        shape.orientation = angfromuvec(self.uvec) - pi/2