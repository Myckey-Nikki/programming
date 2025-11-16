import numpy as np
import matplotlib.pyplot as plt

# --- Parameters of the RLC circuit ---
R = 10          # Resistance in ohms
L = 0.1         # Inductance in henry
C = 100e-6      # Capacitance in farad
V = 1           # Supply voltage in volts

# --- Resonant frequency ---
f0 = 1 / (2 * np.pi * np.sqrt(L * C))
w0 = 2 * np.pi * f0

# --- Quality factor and Bandwidth ---
Q = (1 / R) * np.sqrt(L / C)
BW = f0 / Q

# --- Frequency range ---
f = np.linspace(0, 3 * f0, 1000)
w = 2 * np.pi * f

# --- Impedance and Current ---
Z = np.sqrt(R**2 + (w*L - 1/(w*C))**2)
I = V / Z

# --- Find half-power points (I = Imax / √2) ---
I_max = V / R
I_half = I_max / np.sqrt(2)

# Approximate cutoff frequencies f1, f2
f1 = f0 - BW/2
f2 = f0 + BW/2

# --- Plotting ---
plt.figure(figsize=(8,5))
plt.plot(f, I, label='Current vs Frequency', color='b')
plt.axvline(f0, color='r', linestyle='--', label=f'Resonant f₀ = {f0:.1f} Hz')
plt.axvline(f1, color='g', linestyle='--', label=f'Lower cutoff f₁ = {f1:.1f} Hz')
plt.axvline(f2, color='g', linestyle='--', label=f'Upper cutoff f₂ = {f2:.1f} Hz')
plt.axhline(I_half, color='orange', linestyle=':', label='I = Imax / √2')

# --- Labels ---
plt.title('Resonance in Series RLC Circuit')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Current (A)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# --- Print calculated values ---
print(f"Resonant Frequency f0 = {f0:.2f} Hz")
print(f"Quality Factor Q = {Q:.2f}")
print(f"Bandwidth BW = {BW:.2f} Hz")
print(f"Cutoff Frequencies: f1 = {f1:.2f} Hz, f2 = {f2:.2f} Hz")
