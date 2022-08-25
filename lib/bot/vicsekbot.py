from typing import Callable
import numpy as np

from .bot import Bot

class PlainBot(Bot):
    v = 0.08
    name = "VicsekBot"

    def __init__(self, upf: Callable, upfargs: tuple):
        self.pos = np.array([0, 0])
        self.uvec = np.array([0, 1])
        self.normalizeuvec()
        self.upf = upf
        self.upfargs = upfargs

    def draw(self, ax):
        pass

    def redraw(self, shape):
        pass