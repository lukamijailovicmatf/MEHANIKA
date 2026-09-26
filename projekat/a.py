# a)

import matplotlib.pyplot as plt

F = 400  # [N] - horizontalna pogonska sila
m = 80   # [kg] - masa trkača

F_otpor = 0  # pretpostavka da je otpor vazduha zanemarljiv u ovom delu modela

plt.figure(figsize = (9, 6))

plt.title('Dijagram putanje trkača - samo horizontalne sile')

plt.arrow(0, 0, F, 0, color = 'green', width = 1.3, head_width = 25, label = 'horizontalna pogonska sila')
plt.arrow(F-10, 0, -F_otpor, 0, color = 'blue', width = 1.9, head_width = 18, label = 'otpor vazduha')

plt.grid(True)

plt.xlabel('horizontalna pogonska sila [N]')
plt.ylabel('otpor vazduha')

plt.xlim(-40, 460)
plt.ylim(-40, 40)

plt.show()
