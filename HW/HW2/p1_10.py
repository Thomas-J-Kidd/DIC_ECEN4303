import numpy as np
import matplotlib.pyplot as plt

# Constants
A = 200e-10  # Area in m^2 (200 am^2)
epsilon = 11.9e-12  # Permittivity of silicon in F/m
q = 1.602e-19  # Elementary charge in C
NA = 5e17  # Acceptor doping concentration in cm^-3 (5 x 10^17 cm^-3)
phi_n = 0.56  # Built-in potential in V

# Convert NA to m^-3
NA_m3 = NA * 1e6  # 1 cm^-3 = 1e6 m^-3

# Create an array of reverse-bias voltages from 0 to 2 V
V_reverse_bias = np.linspace(0, 2, 100)

# Calculate junction capacitance for each voltage
Cj = (1 / A) * np.sqrt((2 * epsilon * NA)) / (2*np.sqrt(V_reverse_bias-phi_n))

# Plot the junction capacitance vs. reverse-bias voltage
plt.figure(figsize=(8, 6))
plt.plot(V_reverse_bias, Cj, label='Junction Capacitance')
plt.xlabel('Reverse-Bias Voltage (V)')
plt.ylabel('Junction Capacitance (F)')
plt.title('Junction Capacitance vs. Reverse-Bias Voltage')
plt.grid(True)
plt.legend()
plt.show()

