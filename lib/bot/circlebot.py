import numpy as np
from matplotlib.patches import Circle

from .bot import Bot

# Class for each individual bot. Each one will have
# access to its own position, direction, etc.
class CircleBot(Bot):
    """kwargs:
    - r: sets circlebot collision radius"""
    v = 0.08
    name = "CircleBot"

    def __init__(self, upf, upfargs, r):
        self.pos = np.array([0, 0])
        self.uvec = np.array([0, 1])
        self.normalizeuvec()
        self.upf = upf
        self.upfargs = upfargs
        self.r = r
        self.colliding = False

    def draw(self, ax):
        return ax.add_patch(Circle(self.pos, self.r, fill = False, edgecolor = 'black'))

    def redraw(self, shape):
        shape.center = self.pos
        if self.colliding:
            shape.set_edgecolor('r')
            self.colliding = False
        else:
            shape.set_edgecolor('k')