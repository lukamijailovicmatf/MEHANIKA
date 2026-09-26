# b)

import matplotlib.pyplot as plt

F = 400  # [N] - horizontalna pogonska sila
m = 80   # [kg] - masa trkača

a = F / m  # [m/s^2] - ubrzanje

# Funkcija za izračunavanje položaja trkaca u funkciji od vremena
def pozicija(t):
    # početni položaj
    x0 = 0 
    return 0.5 * a * t**2

# Vremenski trenuci u sekundama
vremenski_trenuci = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Izračunavanje položaja trkača u svakom vremenskom trenutku
pozicije = [pozicija(t) for t in vremenski_trenuci]

plt.figure(figsize = (9, 6))
plt.plot(pozicije, vremenski_trenuci, marker = 's', color = 'r', label = 'položaj trkača')

plt.title('Položaj trkača u vremenskim trenucima')
plt.xlabel('položaj trkača [m]')
plt.ylabel('vreme [s]')

plt.grid(True)
plt.legend()
plt.show()
