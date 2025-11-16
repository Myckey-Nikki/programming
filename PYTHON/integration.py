import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Set up figure
fig = plt.figure(figsize=(15, 5))

# ---------------------------
# 1️⃣ Single Integral (1D)
# ---------------------------
ax1 = fig.add_subplot(131)
x = np.linspace(0, 2, 200)
y = x**2
ax1.plot(x, y, 'b', label='y = x²')
ax1.fill_between(x, y, color='skyblue', alpha=0.4)
ax1.set_title("Single Integral → Area under a curve")
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.legend()

# ---------------------------
# 2️⃣ Double Integral (2D)
# ---------------------------
ax2 = fig.add_subplot(132, projection='3d')
x = np.linspace(0, 2, 40)
y = np.linspace(0, 2, 40)
X, Y = np.meshgrid(x, y)
Z = X + Y
ax2.plot_surface(X, Y, Z, cmap='viridis', alpha=0.7)
ax2.set_title("Double Integral → Volume under a surface")
ax2.set_xlabel("x")
ax2.set_ylabel("y")
ax2.set_zlabel("z")

# Draw projection (the region of integration)
ax2.plot_surface(X, Y, np.zeros_like(Z), color='gray', alpha=0.2)

# ---------------------------
# 3️⃣ Triple Integral (3D Volume)
# ---------------------------
ax3 = fig.add_subplot(133, projection='3d')
# Define a cube region
r = [0, 1]
for s, e in zip(r, r[::-1]):
    X, Y = np.meshgrid(r, r)
    ax3.plot_surface(X, Y, np.full_like(X, s), alpha=0.3, color='orange')  # top/bottom
    ax3.plot_surface(X, np.full_like(X, s), Y, alpha=0.3, color='orange')  # front/back
    ax3.plot_surface(np.full_like(X, s), X, Y, alpha=0.3, color='orange')  # sides
ax3.set_title("Triple Integral → Volume of a 3D region")
ax3.set_xlabel("x")
ax3.set_ylabel("y")
ax3.set_zlabel("z")
ax3.text(0.3, 0.3, 0.5, "dV", fontsize=12, color='red')

plt.tight_layout()
plt.show()
