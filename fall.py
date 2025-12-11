import numpy as np
import matplotlib.pyplot as plt

# Datos iniciales
r1 = np.array([0., 0.])
r2 = np.array([1., 0.])
v1 = np.array([0., 0.2])
v2 = np.array([0., -0.1])

G = 1.0
dt = 0.01
positions1, positions2 = [], []

for _ in range(150):
    # Vector de separación
    r = r2 - r1
    dist = np.linalg.norm(r)
    force = G * r / dist**3

    # Actualización de velocidades y posiciones
    v1 += force * dt
    v2 -= force * dt
    r1 += v1 * dt
    r2 += v2 * dt

    positions1.append(r1.copy())
    positions2.append(r2.copy())

positions1 = np.array(positions1)
positions2 = np.array(positions2)

plt.plot(positions1[:,0], positions1[:,1])
plt.plot(positions2[:,0], positions2[:,1])
plt.show()
