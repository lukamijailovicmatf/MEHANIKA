# g)

import numpy as np
import matplotlib.pyplot as plt

# konstante
F = 400  # [N] - horizontalna pogonska sila
rho = 1.293  # [kg/m^3] - gustina vazduha na nivou mora
Cd = 1.2  # koeficijent otpora
A = 0.45  # [m^2] - poprečni presek trkača

# Računamo teorijsku maksimalnu brzinu
V_T = np.sqrt(2 * F / (rho * Cd * A))

print("Teorijska maksimalna brzina trkača:", V_T, "m/s")

# Grafik za prikaz teorijske maksimalne brzine
plt.plot([0, V_T], [0, 1], 'r--')
plt.xlabel('brzina [m/s]')
plt.ylabel('vreme [s]')
plt.title('Teorijska maksimalna brzina trkača')
plt.grid(True)
plt.show()

##############################################################################################################
#mozda cu izbrisati grafik


# Da bismo pronašli teorijsku maksimalnu brzinu trkača pod dejstvom dati sila, koristićemo formulu:
# vT=2FρCDAvT​=ρCD​A2F​

# Gde su:
#     FF = 400 N (konstantna horizontalna pogonska sila)
#     ρρ = 1.293 kg/m³ (gustina vazduha na nivou mora)
#     CDCD​ = 1.2 (koeficijent otpora)
#     AA = 0.45 m² (poprečna površina trkača)

# Sada samo zamenimo ove vrednosti u formulu i izračunamo vTvT​:

# vT=2×4001.293×1.2×0.45vT​=1.293×1.2×0.452×400​

# ​

# vT=8000.70155vT​=0.70155800​

# ​

# vT≈1140.294≈33.75 m/svT​≈1140.294

# ​≈33.75m/s

# Dakle, teorijska maksimalna brzina trkača pod dejstvom ovih sila iznosi otprilike 33.75 m/s.

# Sada ću implementirati ovo rešenje koristeći Python. Da li preferirate da koristim neku specifičnu biblioteku za 
# matematiku ili grafikone?