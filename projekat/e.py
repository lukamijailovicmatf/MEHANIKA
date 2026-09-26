# e)

import numpy as np
import matplotlib.pyplot as plt

# konstante
F = 400  # pogonska sila [N]
m = 80   # masa trkača [kg]
rho = 1.293  # gustina vazduha na nivou mora [kg/m^3]
A = 0.45   # presečna površina trkača [m^2]
Cd = 1.2   # koeficijent otpora vazduha
w = 0     # brzina vetra [m/s]
x0 = 0    # početni položaj [m]
v0 = 0    # početna brzina [m/s]
t0 = 0    # početno vreme [s]
t_kraj = 10  # krajnje vreme [s]
dt = 0.01  # korak vremena [s]

# Funkcija za ubrzanje
def ubrzanje(v):

    # otpor vazduha
    D = 0.5 * rho * Cd * A * (v - w) ** 2

    # ubrzanje 
    a = (F - D) / m 

    return a

# Ojlerova metoda za pronalaženje brzine i položaja
def ojlerov_metod():

    t = [t0]
    x = [x0]
    v = [v0]
    a = [ubrzanje(v0)]

    while t[-1] < t_kraj:
        v.append(v[-1] + a[-1] * dt)
        x.append(x[-1] + v[-1] * dt)
        a.append(ubrzanje(v[-1]))
        t.append(t[-1] + dt)

    return t, x, v, a

# Poziv funkcije za Ojlerovu metodu
t, x, v, a = ojlerov_metod()

# Plotovanje rezultata
plt.figure(figsize = (12, 8))
plt.subplot(3, 1, 1)
plt.plot(t, x, 'red')
plt.title('Položaj trkača u funkciji od vremena')
plt.xlabel('vreme [s]')
plt.ylabel('položaj [m]')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(t, v, 'orange')
plt.title('Brzina trkača u funkciji od vremena')
plt.xlabel('vreme [s]')
plt.ylabel('brzina [m/s]')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(t, a, 'green')
plt.title('Ubrzanje trkača u funkciji od vremena')
plt.xlabel('vreme [s]')
plt.ylabel('ubrzanje [m/s^2]')
plt.grid(True)

plt.tight_layout()
plt.show()
