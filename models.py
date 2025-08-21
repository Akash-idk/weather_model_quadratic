import matplotlib.pyplot as plt
import numpy as np

# Coefficients for quadratic model
a, b, c = 0.4, -2.5, 26

def quadratic_weather_model(time):
    """Predict temperature using quadratic equation."""
    return a * (time ** 2) + b * time + c

# Generate time points
days = np.arange(0, 25, 1)  # every hour from 0–24

# ===== WATERFALL MODE =====
temps_waterfall = [quadratic_weather_model(t) for t in days]

plt.figure(figsize=(14, 8))

# Top plot: Waterfall
plt.subplot(2, 1, 1)
plt.plot(days, temps_waterfall, 'bo-', label=f"T = {a}t² + {b}t + {c}")
plt.title("Weather Modeling (Quadratic Model)")
plt.xlabel("Time (hours)")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True)

# ===== ITERATIVE MODE =====
plt.subplot(2, 2, 3)
for iteration in range(1, 4):
    hours = np.arange(0, 25, 12)  # every 12 hours
    temps = [quadratic_weather_model(t) for t in hours]
    plt.plot(hours, temps, marker='o', label=f"Iteration {iteration}")
plt.title("Iterative Model Weather Curve")
plt.xlabel("Time (hours)")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True)

# ===== AGILE MODE =====
plt.subplot(2, 2, 4)
times_to_check = [0, 6, 12, 18, 24]
for sprint in range(1, 3):
    temps = [quadratic_weather_model(t) for t in times_to_check]
    plt.plot(times_to_check, temps, marker='o', label=f"Sprint {sprint}")
plt.title("Agile Model Weather Curve")
plt.xlabel("Time (hours)")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()