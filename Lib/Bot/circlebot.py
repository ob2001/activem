from ..lib import np, randbw, rotvec, distance, angle, vecdiffr, sees
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

    def collision(self, botb):
        collang = np.pi
        d = distance(self.pos, botb.pos)
        if(d < self.r and angle(self.uvec, vecdiffr(self.pos, botb.pos, 1)) < collang and sees(self.pos, self.uvec, collang, botb.pos)[0]):
            vec = vecdiffr(self.pos, botb.pos, (self.r - d)/2)
            botb.pos += vec
            self.pos -= vec

    def draw(self, ax):
        ax.add_patch(Circle((self.pos[0], self.pos[1]), self.r/2, fill = False, edgecolor = 'black'))