import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # 3D plotting

# Parameters
g = 9.8  #gravity
v0 = float(input("Enter the initial velocity (m/s): "))
angle_deg = float(input("Enter the launch angle in the XY plane (deg.): "))
phi_deg = float(input("Enter the azimuth angle (XZ plane, deg.): "))

# Make sure that the angles are within 360 degrees to fit in the plot
if angle_deg > 360:
    t = int(angle_deg // 360)
    for i in range(t):
        angle_deg = angle_deg - 360
if phi_deg > 360:
    t = int(phi_deg // 360)
    for i in range(t):
        phi_deg = phi_deg - 360

# Convert angles to radians
angle_rad = math.radians(angle_deg)
phi_rad = math.radians(phi_deg)

# Initial velocity components
v0_x = v0 * math.cos(angle_rad) * math.cos(phi_rad)
v0_y = v0 * math.sin(angle_rad)
v0_z = v0 * math.cos(angle_rad) * math.sin(phi_rad)

# Time of flight
time_of_flight = (2 * v0_y) / g

# Generate trajectory points
dt = 0.01  # Time step
t = 0
x, y, z = [], [], []

while t <= time_of_flight:
    x_pos = v0_x * t
    y_pos = v0_y * t - 0.5 * g * t ** 2
    z_pos = v0_z * t
    if y_pos < 0:  # Stop when projectile hits the ground
        break
    x.append(x_pos)
    y.append(y_pos)
    z.append(z_pos)
    t += dt

# Plotting the 3D trajectory
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

ax.plot(x, z, y, label="Projectile Trajectory")  
ax.set_title("3D Projectile Motion Simulation")
ax.set_xlabel("X-axis (Horizontal Distance)")
ax.set_ylabel("Z-axis (Side Distance)")
ax.set_zlabel("Y-axis (Vertical Height)")
ax.legend()
plt.show()
