import numpy as np
import random

""" Functions """
# Return the unit vector in the same direction as the
# input vector
def normalize(t):
    return t/np.linalg.norm(t)

# Return a random number with specified resolution in
# specified range
def randbw(a):
    return random.uniform(-a, a)

# Returns Cartesian distance between two points
def distance(r1, r2):
    return np.sqrt((r2[0] - r1[0])**2 + (r2[1] - r1[1])**2)

# Return the unit vector pointing from r1 to r2
def vecdiffn(r1, r2):
    return (r2 - r1)/np.linalg.norm(r2 - r1)

# Return the vector of length r pointing from r1 to r2
def vecdiffr(r1, r2, r):
    return r*vecdiffn(r1, r2)

# Returns a unit vector pointing in the direction
# of the angle theta (radians)
def uvecfromang(theta):
    return np.cos(theta), np.sin(theta)

# Returns the angle of a unit vector with respect
# to the x-axis
def angfromuvec(v):
    return np.arctan2(v[1], v[0])

# Rotate the given vector v by the angle theta in the
# CCW direction
def rotvec(v, theta):
    return [[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]]@v