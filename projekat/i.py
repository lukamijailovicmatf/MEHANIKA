# i)

import numpy as np
import matplotlib.pyplot as plt

# konstante
F = 400  # [N] - horizontalna pogonska sila
m = 80  # [kg] - masa trkača
rho = 1.293  # [kg/m^3] - gustina vazduha na nivou mora
A = 0.45  # [m^2] - presečna površina trkača
Cd = 1.2  # koeficijent otpora vazduha
w = 0  # [m/s] - brzina vetra
fv = 25.8  # [sN/m]
fc = 488  # [N]
tc = 0.67  # [s]
g = 9.81  # [m/s^2] - ubrzanje

# Ojlerova metoda
def ojlerova_metoda(dt, vremenski_trenuci):

    t = np.zeros(vremenski_trenuci)
    v = np.zeros(vremenski_trenuci)
    x = np.zeros(vremenski_trenuci)
    a = np.zeros(vremenski_trenuci)

    for i in range(1, vremenski_trenuci):

        Fv = -fv * v[i-1]
        FC = fc * np.exp(-(t[i-1] / tc)**2)
        D = 0.5 * A * rho * Cd * (v[i-1] - w) * 2 * (1 - 0.25 * np.exp(-(t[i-1] / tc) * 2))
        Fnet = F + FC - Fv - D

        a[i-1] = Fnet / m
        v[i] = v[i-1] + a[i-1] * dt
        x[i] = x[i-1] + v[i-1] * dt
        t[i] = t[i-1] + dt

    return t, x, v, a

# Parametri za numeričku integraciju
dt = 0.01  # vremenski korak
vremenski_trenuci = 1000  # broj koraka

# Poziv funkcije "ojlerova_metoda"
t, x, v, a = ojlerova_metoda(dt, vremenski_trenuci)

# Prikaz rezultata
plt.figure(figsize = (12, 8))
plt.subplot(3, 1, 1)
plt.plot(t, x, 'red')
plt.title('Pozicija x(t)')
plt.xlabel('vreme [s]')
plt.ylabel('pozicija [m]')

plt.subplot(3, 1, 2)
plt.plot(t, v, 'orange')
plt.title('Brzina v(t)')
plt.xlabel('vreme [s]')
plt.ylabel('brzina [m/s]')

plt.subplot(3, 1, 3)
plt.plot(t, a, 'green')
plt.title('Ubrzanje a(t)')
plt.xlabel('vreme [s]')
plt.ylabel('ubrzanje [m/s^2]')

plt.tight_layout()
plt.show()