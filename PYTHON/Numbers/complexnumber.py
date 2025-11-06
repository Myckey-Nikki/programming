import numpy as np
import matplotlib.pyplot as plt

# Domain
x = np.linspace(-4*np.pi, 4*np.pi, 2000)

# Complex function f(x) = e^{i x}
f = np.exp(1j * x)

# Components
real = np.real(f)
imag = np.imag(f)
modulus = np.abs(f)           # |e^{i x}| = 1
arg_wrapped = np.angle(f)     # in (-pi, pi]
arg_unwrapped = np.unwrap(arg_wrapped)

# Plot: real & imaginary parts
plt.figure(figsize=(10, 6))
plt.plot(x, real, label='Re(f) = cos(x)')
plt.plot(x, imag, label='Im(f) = sin(x)')
plt.title('Real and Imaginary Parts of f(x) = e^{i x}')
plt.xlabel('x')
plt.ylabel('value')
plt.grid(True, alpha=0.3)
plt.legend()

# Plot: modulus
plt.figure(figsize=(10, 3))
plt.plot(x, modulus, color='purple')
plt.title('Modulus |f(x)|')
plt.xlabel('x')
plt.ylabel('|f(x)|')
plt.ylim(0.9, 1.1)
plt.grid(True, alpha=0.3)

# Plot: argument (wrapped)
plt.figure(figsize=(10, 4))
plt.plot(x, arg_wrapped, color='darkgreen')
plt.title('Argument arg(f(x)) (wrapped to (-π, π])')
plt.xlabel('x')
plt.ylabel('arg(f)')
plt.yticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
           [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$\pi/2$', r'$\pi$'])
plt.grid(True, alpha=0.3)

# Plot: argument (unwrapped)
plt.figure(figsize=(10, 4))
plt.plot(x, arg_unwrapped, color='orange')
plt.title('Argument arg(f(x)) (unwrapped)')
plt.xlabel('x')
plt.ylabel('arg(f)')
plt.grid(True, alpha=0.3)

plt.show()