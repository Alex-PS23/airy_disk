"""
This file creates a model of an Airy disk with
a circular slit diameter increasing over time.
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.special
from matplotlib.animation import ArtistAnimation

n = 1000
L = 2
s = np.linspace(-L, L, n)

fx = 0.5
fy = 0.5

h_arr = np.arange(0.01, 20, 0.01)
frames = []

fig, ax = plt.subplots(figsize=(6, 6))

for h in h_arr:
    sxgrid, sygrid = np.meshgrid(s, s)
    zgrid = np.sqrt(sxgrid ** 2 + sygrid ** 2)
    a = np.sqrt(np.power((scipy.special.fresnel(zgrid + h)[1] - scipy.special.fresnel(zgrid - h)[1]), 2) +
                np.power((scipy.special.fresnel(zgrid + h)[0] - scipy.special.fresnel(zgrid - h)[0]), 2))
    line = ax.imshow(a, cmap='gray', vmin=0, vmax=1.8)
    frames.append([line])
    print(h)

plt.axis('off')
fig.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0)

animation = ArtistAnimation(
    fig,
    frames,
    interval=30,
    blit=True,
    repeat=True)

animation.save('Airy_disk.mp4')

plt.show()
