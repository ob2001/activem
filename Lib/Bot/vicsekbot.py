from .bot import Bot

class VicsekBot(Bot):
    v = 0.08
    name = "VicsekBot"

    def __init__(self, upf, upfargs):
        self.pos = [0, 0]
        self.uvec = [0, 1]
        self.normalizeuvec()
        self.upf = upf
        self.upfargs = upfargs

    def draw(self, ax):
        pass

    def redraw(self, shape):
        pass