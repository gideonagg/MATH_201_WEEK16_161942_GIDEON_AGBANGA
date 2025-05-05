import numpy as np
from scipy.integrate import quad

def integrand(x):
    ln_x = np.log(x)
    return (1 + ln_x) * np.sqrt(1 + (x * ln_x)**2)

integral_value, error = quad(integrand, 0.2, 1)

print(f"Integral value: {integral_value:.6f}")
print(f"Error estimate: {error:.2e}")