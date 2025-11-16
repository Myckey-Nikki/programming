import numpy as np
import matplotlib.pyplot as plt

# Parameters
wn = 1000       # natural frequency (rad/s)
zeta = 0.2      # damping ratio

# Frequency range (logarithmic)
w = np.logspace(1, 5, 1000)
s = 1j * w

# Transfer function H(jw)
H = (wn**2) / (s**2 + 2*zeta*wn*s + wn**2)

# Magnitude (dB) and Phase (degrees)
mag = 20 * np.log10(np.abs(H))
phase = np.angle(H, deg=True)

# --- Important frequencies ---
# Resonant peak (if zeta < 1/sqrt(2))
if zeta < 1/np.sqrt(2):
    wr = wn * np.sqrt(1 - 2*zeta**2)
    Mr = 1 / (2*zeta * np.sqrt(1 - zeta**2))
    Mr_db = 20 * np.log10(Mr)
else:
    wr, Mr_db = None, None

# Bandwidth (approximation)
wB = 2 * zeta * wn

# --- Plot Magnitude ---
plt.figure(figsize=(10,6))
plt.subplot(2,1,1)
plt.semilogx(w, mag, label='Magnitude (Exact)')
plt.axvline(wn, color='r', linestyle=':', label='ωₙ (Corner)')

if wr:
    plt.axvline(wr, color='g', linestyle='--', label='ωᵣ (Resonant)')
    plt.axhline(Mr_db, color='g', linestyle='--', label=f'Mᵣ = {Mr_db:.2f} dB')

plt.axvline(wB, color='m', linestyle='--', label='ω_B (Bandwidth)')
plt.ylabel('Magnitude (dB)')
plt.title('Bode Plot for Second-Order System')
plt.legend()
plt.grid(True, which='both')

# --- Plot Phase ---
plt.subplot(2,1,2)
plt.semilogx(w, phase, color='orange')
plt.axvline(wn, color='r', linestyle=':')
plt.axvline(wB, color='m', linestyle='--')
plt.ylabel('Phase (degrees)')
plt.xlabel('Frequency (rad/s)')
plt.grid(True, which='both')

plt.tight_layout()
plt.show()
