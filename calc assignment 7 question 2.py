#Area by Monte Carlo simulation
import numpy as np

# Define the line function
def line(x):
    return (-3 / (7 * np.pi)) * x

# Define the bounding box
x_min, x_max = 0, 7 * np.pi / 6
y_min = -0.5  # from the line
y_max = 1.0   # max of sin(x)

# Number of random points
N = 1000000

# Generate random points
x_points = np.random.uniform(x_min, x_max, N)
y_points = np.random.uniform(y_min, y_max, N)

# Count points between the two curves
points_under_sin = y_points <= np.sin(x_points)
points_above_line = y_points >= line(x_points)
points_in_area = points_under_sin & points_above_line

# Calculate area
total_area = (x_max - x_min) * (y_max - y_min)
monte_carlo_area = total_area * np.sum(points_in_area) / N

# Output
print(f"✅ Area by Monte Carlo simulation: {monte_carlo_area:.6f}")
print(f"with {N:,} points")
