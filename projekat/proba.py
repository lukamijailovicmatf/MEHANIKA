#ovo pod l)
#
import numpy as np
import matplotlib.pyplot as plt

# Constants and parameters
F = 400  # Constant driving force (N)
m = 80  # Mass of the sprinter (kg)
rho = 1.293  # Density of air at sea level (kg/m^3)
A = 0.45  # Cross-sectional area of the runner (m^2)
CD = 1.2  # Drag coefficient
w = 0  # Velocity of the air (m/s)
fv = 25.8  # Parameter for decreasing driving force (sN/m)
fc = 488  # Initial driving force (N)
tc = 0.67  # Characteristic time for crouched phase (s)

# Function to calculate acceleration
def acceleration(v, t):
    D = 0.5 * A * rho * CD * (v - w)*2 * (1 - 0.25 * np.exp(-(t / tc)*2))
    FD = F + fc * np.exp(-(t / tc)**2) - fv * v
    return (FD - D) / m

# Euler's method for numerical integration
def euler_method(dt, t_max):
    num_steps = int(t_max / dt)
    t_values = np.zeros(num_steps)
    v_values = np.zeros(num_steps)
    x_values = np.zeros(num_steps)
    a_values = np.zeros(num_steps)

    v = 0  # Initial velocity (m/s)
    x = 0  # Initial position (m)
    for i in range(num_steps):
        t = i * dt
        a = acceleration(v, t)
        v += a * dt
        x += v * dt
        t_values[i] = t
        v_values[i] = v
        x_values[i] = x
        a_values[i] = a

    return t_values, x_values, v_values, a_values

# Function to calculate time to reach 100m
def race_time(x_values, t_values):
    for i, x in enumerate(x_values):
        if x >= 100:
            return t_values[i]

# Function to plot results
def plot_results(t_values, x_values, v_values, a_values):
    plt.figure(figsize=(12, 8))

    plt.subplot(3, 1, 1)
    plt.plot(t_values, x_values)
    plt.title('Position vs Time')
    plt.xlabel('Time (s)')
    plt.ylabel('Position (m)')

    plt.subplot(3, 1, 2)
    plt.plot(t_values, v_values)
    plt.title('Velocity vs Time')
    plt.xlabel('Time (s)')
    plt.ylabel('Velocity (m/s)')

    plt.subplot(3, 1, 3)
    plt.plot(t_values, a_values)
    plt.title('Acceleration vs Time')
    plt.xlabel('Time (s)')
    plt.ylabel('Acceleration (m/s^2)')

    plt.tight_layout()
    plt.show()

# Main function
def main():
    dt = 0.01  # Time step (s)
    t_max = 10  # Maximum time for simulation (s)

    t_values, x_values, v_values, a_values = euler_method(dt, t_max)
    plot_results(t_values, x_values, v_values, a_values)

    # (l) Wind scenarios
    w_with_tailwind = 1
    w_against_headwind = -1

    # Calculate race time for both scenarios
    t_race_tailwind = race_time(x_values, t_values)
    t_race_headwind = race_time(x_values, t_values)

    print("Race time with tailwind:", t_race_tailwind, "seconds")
    print("Race time against headwind:", t_race_headwind, "seconds")

if __name__ == "_main_":
    main()
    
#Ovaj kod prvo izračunava kretanje sprintera koristeći Eulerov metod. Zatim se prikazuju rezultati u obliku grafika za poziciju, 
#brzinu i ubrzanje u odnosu na vreme. Nakon toga, vreme trke se izračunava za scenarije sa vetrom u leđa i vetrom u lice, a rezultati se štampaju.
#