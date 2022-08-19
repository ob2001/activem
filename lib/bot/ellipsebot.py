from ..fs import np, rotvec, angfromuvec
from .bot import Bot
from matplotlib.patches import Ellipse

class EllipseBot(Bot):
    v = 0.08
    name = "EllipseBot"

    def __init__(self, upf, upfargs, a = 1.5, b = 0.25):
        self.a, self.b = a, b
        self.pos = np.array([0, 0])
        self.uvec = np.array([0, 1]) # Points in direction of major axis
        self.normalizeuvec()
        self.upf = upf
        self.upfargs = upfargs
        self.colliding = False

    def getuarr(self):
        ovec = rotvec(self.uvec, -np.pi/2)
        return np.array([[self.uvec[0], ovec[0]], [self.uvec[1], ovec[1]]])

    def getA(self):
        uarr = self.getuarr()
        sigarr = np.array([[1/self.a**2, 0], [0, 1/self.b**2]])
        return uarr@sigarr@uarr.T

    def draw(self, ax):
        return ax.add_patch(Ellipse(self.pos, self.a, self.b, fill = False, angle = np.rad2deg(angfromuvec(self.uvec))))

    def redraw(self, shape):
        shape.center = self.pos
        shape.angle = np.rad2deg(angfromuvec(self.uvec))
        if self.colliding:
            shape.set_edgecolor('r')
            self.colliding = False
        else:
            shape.set_edgecolor('k')