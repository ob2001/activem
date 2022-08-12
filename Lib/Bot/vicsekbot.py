from ..lib import np, randbw, rotvec, distance, angle, vecdiffr, sees
from .bot import Bot

class VicsekBot(Bot):
    v = 0.08
    name = "VicsekBot"

    def __init__(self, W, H, upf, upfargs, **kwargs):
        self.pos = [randbw(W), randbw(H)]
        self.uvec = [randbw(1), randbw(1)]
        self.normalizeuvec()
        self.upf = upf
        self.upfargs = upfargs

    def collision(self, botb):
        pass

    def draw(self, ax):
        pass