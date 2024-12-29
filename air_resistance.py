import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants
g = 9.8  # Acceleration due to gravity (m/s^2)
rho = 1.225  # Air density (kg/m^3)
Cd = 0.47  # Drag coefficient (for a sphere)
radius = 0.05  # Radius of the projectile (m)
area = math.pi * radius**2  # Cross-sectional area (m^2)
mass = 1.0  # Mass of the projectile (kg)
dt = 0.01  # Time step for numerical simulation

# Inputs
v0 = float(input("Enter the initial velocity (m/s): "))
launch_angle_deg = float(input("Enter the launch angle (degrees): "))
azimuth_angle_deg = float(input("Enter the azimuth angle (degrees): "))
# Make sure that the angles are within 360 degrees to fit in the plot
if launch_angle_deg > 360:
    t = int(launch_angle_deg // 360)
    for i in range(t):
        launch_angle_deg = launch_angle_deg - 360
if azimuth_angle_deg > 360:
    t = int(azimuth_angle_deg // 360)
    for i in range(t):
        azimuth_angle_deg = azimuth_angle_deg - 360
# Convert angles to radians
launch_angle_rad = math.radians(launch_angle_deg)
azimuth_angle_rad = math.radians(azimuth_angle_deg)

# Initial velocity components
v0_x = v0 * math.cos(launch_angle_rad) * math.cos(azimuth_angle_rad)
v0_y = v0 * math.sin(launch_angle_rad)
v0_z = v0 * math.cos(launch_angle_rad) * math.sin(azimuth_angle_rad)

# Function to simulate motion without air resistance
def simulate_no_air_resistance():
    x, y, z = 0, 0, 0
    vx, vy, vz = v0_x, v0_y, v0_z
    trajectory_x, trajectory_y, trajectory_z = [x], [y], [z]

    while y >= 0:
        x += vx * dt
        y += vy * dt
        z += vz * dt
        vy -= g * dt  # Only gravity affects vertical motion
        trajectory_x.append(x)
        trajectory_y.append(y)
        trajectory_z.append(z)

    return trajectory_x, trajectory_y, trajectory_z

# Function to simulate motion with air resistance
def simulate_with_air_resistance():
    x, y, z = 0, 0, 0
    vx, vy, vz = v0_x, v0_y, v0_z
    trajectory_x, trajectory_y, trajectory_z = [x], [y], [z]

    while y >= 0:
        # Compute speed and drag force
        speed = math.sqrt(vx**2 + vy**2 + vz**2)
        drag_force = 0.5 * rho * Cd * area * speed**2

        # Decompose drag force into components
        drag_force_x = -drag_force * (vx / speed)
        drag_force_y = -drag_force * (vy / speed)
        drag_force_z = -drag_force * (vz / speed)

        # Update acceleration
        ax = drag_force_x / mass
        ay = (drag_force_y / mass) - g
        az = drag_force_z / mass

        # Update velocity
        vx += ax * dt
        vy += ay * dt
        vz += az * dt

        # Update position
        x += vx * dt
        y += vy * dt
        z += vz * dt

        trajectory_x.append(x)
        trajectory_y.append(y)
        trajectory_z.append(z)

    return trajectory_x, trajectory_y, trajectory_z

# Simulate both cases
x_no_air, y_no_air, z_no_air = simulate_no_air_resistance()
x_with_air, y_with_air, z_with_air = simulate_with_air_resistance()

# 3D Plotting
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot no air resistance trajectory
ax.plot(x_no_air, z_no_air, y_no_air, label="Without Air Resistance", linestyle="--", color="blue")

# Plot air resistance trajectory
ax.plot(x_with_air, z_with_air, y_with_air, label="With Air Resistance", linestyle="-", color="red")

# Labels and title
ax.set_title("3D Projectile Motion: With and Without Air Resistance")
ax.set_xlabel("Horizontal Distance (x) (m)")
ax.set_ylabel("Lateral Distance (z) (m)")
ax.set_zlabel("Vertical Distance (y) (m)")
ax.legend()
plt.show()
