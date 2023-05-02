import numpy as np
import random

""" Functions """
# Return the unit vector in the same direction as the
# input vector
def normalize(t: np.ndarray) -> np.ndarray:
    return t/np.linalg.norm(t)

# Return a random number with specified resolution in
# specified range
def randbw(a: float, b = None) -> float:
    if b is None:
        return random.uniform(-a, a)
    else:
        return random.uniform(a, b)

# Returns Cartesian distance between two points
def distance(r1: np.ndarray, r2: np.ndarray) -> float:
    return np.sqrt((r2[0] - r1[0])**2 + (r2[1] - r1[1])**2)

# Return the unit vector pointing from r1 to r2
def vecdiffn(r1: np.ndarray, r2: np.ndarray) -> np.ndarray:
    return (r2 - r1)/np.linalg.norm(r2 - r1)

# Return the vector of length r pointing from r1 to r2
def vecdiffr(r1: np.ndarray, r2: np.ndarray, r: float) -> np.ndarray:
    return r*vecdiffn(r1, r2)

# Returns a unit vector pointing in the direction
# of the angle theta (radians)
def uvecfromang(theta: float) -> np.ndarray:
    return np.cos(theta), np.sin(theta)

# Returns the angle of a unit vector with respect
# to the x-axis
def angfromuvec(v: np.ndarray) -> float:
    return np.arctan2(v[1], v[0])

# Rotate the given vector v by the angle theta in the
# CCW direction
def rotvec(v: np.ndarray, theta: float) -> np.ndarray:
    return [[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]]@v