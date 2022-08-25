from typing import Callable
import numpy as np
from matplotlib.pyplot import Axes
from matplotlib.patches import Patch, RegularPolygon

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

    def draw(self, ax: Axes) -> Patch:
        return ax.add_patch(RegularPolygon(self.pos, 3, self.r, angfromuvec(self.uvec) - np.pi/2, fill = False))

    def redraw(self, shape: Patch):
        shape.xy = self.pos
        shape.orientation = angfromuvec(self.uvec) - np.pi/2