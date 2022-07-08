import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

""" Functions """
# Return the unit vector in the same direction as the
# input vector
def normalize(t):
    return t/np.linalg.norm(t)

# Return a random number with specified resolution in
# specified range
def randbw(a, res):
    return random.randint(-res*a, res*a)/res

# Returns Cartesian distance between two points
def distance(r1, r2):
    return np.sqrt((r2[0] - r1[0])**2 + (r2[1] - r1[1])**2)

# Returns the angle between two vectors
def angle(r1, r2):
    return np.arccos(r1@r2/np.sqrt(r1@r1*r2@r2))

# Returns True if point is in vision cone
# Returns False otherwise
def sees(r1, u1, thetavis, r2):
    phi = angle(u1 - r1, r2 - r1)
    return [True, phi] if phi < thetavis else [False, 0.]

# Return a vector of length r pointing from r1 to r2
def vecdiffr(r1, r2, r):
    return r*(r2 - r1)/np.linalg.norm(r2 - r1)

# Returns a unit vector pointing in the direction
# of the angle theta (radians)
def uvecfromang(theta):
    return np.cos(theta), np.sin(theta)

# Returns a unit vector pointing in the direction
# of the angle theta (degrees)
def uvecfromangd(theta):
    return np.cos(np.deg2rad(theta)), np.sin(np.deg2rad(theta))

# Returns the angle of a unit vector with respect
# to the x-axis
def angfromuvecd(v):
    return np.arctan2(v[0], v[1])