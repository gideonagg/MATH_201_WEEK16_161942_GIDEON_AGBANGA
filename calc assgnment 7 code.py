# Percentage of income for bottom 50% of households
def L(x):
    return (5/12)*x**2 + (7/12)*x

percentage_50 = L(0.5) * 100
print(f"Percentage of total income received by bottom 50%: {percentage_50:.2f}%")

#coefficient of inequality
import numpy as np
from scipy.integrate import quad

def integrand(x):
    return x - L(x)

area_between, error = quad(integrand, 0, 1)
coefficient = 2 * area_between

print(f"Coefficient of inequality: {coefficient:.6f}")
print(f"Integration error estimate: {error:.2e}")