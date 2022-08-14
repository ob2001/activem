from ..lib import randbw, uvecfromang
from .bot import Bot
from matplotlib.patches import Circle
from numpy import pi

# Class for each individual bot. Each one will have
# access to its own position, direction, etc.
class CircleBot(Bot):
    """kwargs:
    - r: sets circlebot collision radius"""
    v = 0.08
    name = "CircleBot"

    def __init__(self, upf, upfargs, r):
        self.pos = [0, 0]
        self.uvec = [0, 1]
        self.normalizeuvec()
        self.upf = upf
        self.upfargs = upfargs
        self.r = r

    def draw(self, ax):
        ax.add_patch(Circle((self.pos[0], self.pos[1]), self.r, fill = False, edgecolor = 'black'))