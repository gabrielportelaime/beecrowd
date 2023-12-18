import numpy as np
import matplotlib.patches as patches
import matplotlib.pyplot as plt

heptagono = np.linspace(0, 2 * np.pi, 8)
pontos = np.vstack((np.cos(heptagono), np.sin(heptagono))).transpose()

plt.gca().add_patch(patches.Polygon(pontos, color = '.3'))
plt.grid(True)
plt.axis('scaled')
plt.show()