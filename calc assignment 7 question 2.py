import numpy as np
from scipy.optimize import fsolve
from scipy.integrate import quad

def line(x):
    return (-3/(7*np.pi))*x

def difference(x):
    return np.sin(x) - line(x)

# Find intersection point besides x=0
x_intersect = fsolve(difference, 3)[0]  # initial guess near π

# Calculate area
def integrand(x):
    return np.sin(x) - line(x)

area_integral, error = quad(integrand, 0, x_intersect)
print(f"Area by integral definition: {area_integral:.6f}")
print(f"Intersection point: x = {x_intersect:.6f}")