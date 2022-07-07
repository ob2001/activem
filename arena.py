from lib import *

# Class for the arena in which the bots are interacting.
# Mainly just a container for x and y bounds
class Arena:
    def __init__(self, h, w):
        self.h = h
        self.w = w
        self.boundsup()

    # Update the variables used for plot bounds if/when the
    # arena bounds are changed
    def boundsup(self):
        self.dh, self.dw = self.h + self.h/10, self.w + self.w/10