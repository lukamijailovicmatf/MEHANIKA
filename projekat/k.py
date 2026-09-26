# k)

import numpy as np
import matplotlib.pyplot as plt

# Parametri trke
F = 400  # [N] - konstantna sila
fc = 488  # [N] - početna sila
fv = 25.8  # [sN/m] - koeficijent koji opisuje smanjenje sile sa povećanjem brzine
tc = 0.67  # [s] - karakteristično vreme
rho = 1.293  # [kg/m^3] - gustina vazduha
A = 0.45  # [m^2] - poprečna površina trkača
Cd = 1.2  # koeficijent otpora
w = 0  # [m/s] - brzina vetra, pretpostavka da je nema

# vreme trke - generišemo 1000 tačaka između 0 i 10 sekundi
t = np.linspace(0, 10, 1000) 

# računanje sila u funkciji od vremena
FC = fc * np.exp(-(t / tc)**2)
FV = -fv * t
D = 0.5 * A * (1 - 0.25 * np.exp(-(t / tc) * 2)) * rho * Cd * (FV * 2)

# Plotovanje grafikona
plt.figure(figsize = (10, 6))
plt.plot(t, np.ones_like(t) * F, label = 'F (konstantna sila)')
plt.plot(t, FC, label = 'FC (sila zbog položaja)')
plt.plot(t, FV, label = 'FV (sila zbog brzine)')
plt.plot(t, D, label = 'D (sila otpora vazduha)')
plt.xlabel('vreme [s]')
plt.ylabel('sila [N]')
plt.title('Sile koje deluju na trkača tokom trke na 100 metara')
plt.legend()
plt.grid(True)
plt.show()
