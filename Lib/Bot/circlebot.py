from ..lib import np, randbw, rotvec, distance, angle, vecdiffr, sees
from .bot import Bot
from matplotlib.patches import Circle

# Class for each individual bot. Each one will have
# access to its own position, direction, etc.
class CircleBot(Bot):
    v = 0.08
    collrad = 1.0
    name = "CircleBot"

    def __init__(self, W, H, upf, upfargs, **kwargs):
        self.pos = [randbw(W), randbw(H)]
        self.uvec = [randbw(1), randbw(1)]
        self.normalizeuvec()
        self.upf = upf
        self.upfargs = upfargs

    def collision(self, botb):
        collang = np.pi
        d = distance(self.pos, botb.pos)
        if(d < self.collrad and angle(self.uvec, vecdiffr(self.pos, botb.pos, 1)) < collang and sees(self.pos, self.uvec, collang, botb.pos)[0]):
            vec = vecdiffr(self.pos, botb.pos, (self.collrad - d)/2)
            botb.pos += vec
            self.pos -= vec

    def draw(self, ax):
        ax.add_patch(Circle((self.pos[0], self.pos[1]), self.collrad/2, fill = False, edgecolor = 'black'))