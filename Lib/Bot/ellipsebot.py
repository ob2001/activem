from ..lib import np, rotvec, angfromuvecd
from .bot import Bot
from matplotlib.patches import Ellipse

class EllipseBot(Bot):
    v = 0.08
    name = "EllipseBot"

    def __init__(self, upf, upfargs, a = 0.25, b = 1.5):
        self.a, self.b = a, b
        self.pos = [0, 0]
        self.uvec = [0, 1] # Points in direction of major axis
        self.normalizeuvec()
        self.upf = upf
        self.upfargs = upfargs

    # Get bot's ovec
    def getovec(self):
        return rotvec(self.uvec, -np.pi/2)

    def draw(self, ax):
        return ax.add_patch(Ellipse((self.pos[0], self.pos[1]), self.a, self.b, fill = False, angle = 90 + angfromuvecd(self.uvec)))

    def redraw(self, shape):
        shape.center = self.pos[0], self.pos[1]
        shape.angle = 90 + angfromuvecd(self.uvec)