import numpy as np
import matplotlib.pyplot as plt

n = np.arange(1, 101)
a_n = 1/n
b_n = np.cumsum(1/n**2)
limit_b = np.pi**2 / 6

fig, axs = plt.subplots(2, 1, figsize=(10, 8))

# a_n = 1/n
axs[0].plot(n, a_n, 'bo-', markersize=4, label=r'$a_n = 1/n$')
axs[0].axhline(0, color='red', linestyle='--', label='Limit = 0')
axs[0].set_title(r'Convergence of $a_n = 1/n$')
axs[0].set_xlabel('n')
axs[0].set_ylabel(r'$a_n$')
axs[0].legend()
axs[0].grid(True, alpha=0.3)

# b_n = sum 1/k^2
axs[1].plot(n, b_n, 'go-', markersize=4,
            label=r'$b_n = \sum_{k=1}^n \frac{1}{k^2}$')
axs[1].axhline(limit_b, color='red', linestyle='--',
               label=fr'Limit = $\pi^2/6 \approx {limit_b:.4f}$')
axs[1].set_title(r'Convergence of $b_n = \sum_{k=1}^n \frac{1}{k^2}$')
axs[1].set_xlabel('n')
axs[1].set_ylabel(r'$b_n$')
axs[1].legend()
axs[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()