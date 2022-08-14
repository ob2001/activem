from ..lib import np, randbw, rotvec, distance, vecdiffr
from .bot import Bot
from matplotlib.patches import Circle

# Class for each individual bot. Each one will have
# access to its own position, direction, etc.
class CircleBot(Bot):
    """kwargs:
    - r: sets circlebot collision radius"""
    v = 0.08
    name = "CircleBot"

    def __init__(self, W, H, upf, upfargs, **kwargs):
        self.pos = [randbw(W), randbw(H)]
        self.uvec = [randbw(1), randbw(1)]
        self.normalizeuvec()
        self.upf = upf
        self.upfargs = upfargs
        self.r = kwargs['r']

    def draw(self, ax):
        ax.add_patch(Circle((self.pos[0], self.pos[1]), self.r/2, fill = False, edgecolor = 'black'))