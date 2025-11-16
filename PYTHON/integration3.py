import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Create figure
fig = plt.figure(figsize=(18, 6))

# ---------------------------------
# 1️⃣ LINE INTEGRAL (1D)
# ---------------------------------
ax1 = fig.add_subplot(131, projection='3d')

# Helix curve (example path)
t = np.linspace(0, 4*np.pi, 300)
x = np.cos(t)
y = np.sin(t)
z = 0.2 * t

ax1.plot3D(x, y, z, color='crimson', linewidth=3, label=r'Curve $C$')
ax1.scatter(1, 0, 0, color='black', s=40)
ax1.text(1, 0, 0, "Start", color='black')
ax1.text(0, 0, 2.6, r"$\int_C \mathbf{F}\cdot d\mathbf{r}$", fontsize=14, color='crimson')

ax1.set_title("Line Integral (1D Path)", fontsize=13)
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('z')
ax1.legend()

# ---------------------------------
# 2️⃣ SURFACE INTEGRAL (2D)
# ---------------------------------
ax2 = fig.add_subplot(132, projection='3d')

# Parametric surface (paraboloid patch)
u = np.linspace(-1, 1, 50)
v = np.linspace(-1, 1, 50)
U, V = np.meshgrid(u, v)
X = U
Y = V
Z = 0.5 * (U**2 + V**2)

surf = ax2.plot_surface(X, Y, Z, cmap='Blues', alpha=0.8, edgecolor='none')
ax2.text(0, 0, 1.2, r"$\iint_S \mathbf{F}\cdot \mathbf{n}\,dA$", fontsize=14, color='navy')

ax2.set_title("Surface Integral (2D Region)", fontsize=13)
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_zlabel('z')

# ---------------------------------
# 3️⃣ VOLUME INTEGRAL (3D)
# ---------------------------------
ax3 = fig.add_subplot(133, projection='3d')

# Use voxel to draw a cube volume
x, y, z = np.indices((2, 2, 2)) - 0.5
voxels = (x >= -0.5) & (x < 0.5) & (y >= -0.5) & (y < 0.5) & (z >= -0.5) & (z < 0.5)
ax3.voxels(voxels, facecolors='orange', edgecolor='k', alpha=0.4)
ax3.text(0, 0, 1.2, r"$\iiint_V f(x,y,z)\,dV$", fontsize=14, color='darkorange')

ax3.set_title("Volume Integral (3D Region)", fontsize=13)
ax3.set_xlabel('x')
ax3.set_ylabel('y')
ax3.set_zlabel('z')

plt.tight_layout()
plt.show()
