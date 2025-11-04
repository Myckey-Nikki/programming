import numpy as np
import matplotlib.pyplot as plt

def plot_surface_and_grad(f, fx, fy, xlim=(-2,2), ylim=(-2,2)):
    x = np.linspace(xlim[0], xlim[1], 80)
    y = np.linspace(ylim[0], ylim[1], 80)
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)

    # Surface
    fig = plt.figure(figsize=(10,4))
    ax1 = fig.add_subplot(1,2,1, projection='3d')
    ax1.plot_surface(X, Y, Z, linewidth=0, antialiased=True, alpha=0.9)
    ax1.set_title('Surface')

    # Contours + gradient field
    ax2 = fig.add_subplot(1,2,2)
    CS = ax2.contour(X, Y, Z, levels=25)
    ax2.quiver(X[::6,::6], Y[::6,::6], fx(X, Y)[::6,::6], fy(X,Y)[::6,::6])
    ax2.set_title('Contours with gradient vectors (arrows)')
    plt.show()

# Example: saddle f(x,y)=x^2 - y^2
f = lambda x,y: x**2 - y**2
fx = lambda x,y: 2*x
fy = lambda x,y: -2*y
plot_surface_and_grad(f, fx, fy)
