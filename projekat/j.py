# j)

import numpy as np
import matplotlib.pyplot as plt

# konstante
F = 400  # [N] - horizontalna pogonska sila
m = 80  # [kg] - masa trkača
rho = 1.293  # [kg/m^3] - gustina vazduha na nivou mora 
A = 0.45  # [m^2] - presečna površina trkača
Cd = 1.2  # koeficijent otpora vazduha
w = 0  # [m/s]
g = 9.81  # [m/s^2]
fv = 25.8  # [sN/m]
fc = 488  # [N]
tc = 0.67  # [s]

# Funkcije za ubrzanje, brzinu i položaj
def ubrzanje(v, t):
    return (F + fc * np.exp(-(t / tc) * 2) - fv * v - 0.5 * rho * A * Cd * (v - w) * 2) / m

def ojlerova_metoda(ubrzanje, v0, x0, dt, t_kraj):

    v = v0
    x = x0
    vremena = np.arange(0, t_kraj, dt)
    brzine = [v0]
    pozicije = [x0]

    for t in vremena:

        v += ubrzanje(v, t) * dt
        x += v * dt
        brzine.append(v)
        pozicije.append(x)

    return vremena, brzine, pozicije

# Parametri za Ojlerovu metodu
v0 = 0  # [m/s]
x0 = 0  # [m]
dt = 0.01  # [s]
t_kraj = 10  # [s]

# Pokretanje Ojlerove metode
vremena, brzine, pozicije = ojlerova_metoda(ubrzanje, v0, x0, dt, t_kraj)

# Pronalaženje vremena potrebnog za pretrčavanje 100 m
index_100m = np.argmax(np.array(pozicije) >= 100)
vreme_do_100m = vremena[index_100m]

# Ispis rezultata
print("Vreme potrebno trkaču da pretrči 100 m:", round(vreme_do_100m, 2), "s")