import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df = pd.read_csv("April.csv", sep=",", header=0)
x = df["start_lat"]
y = df["end_lat"]


X, Y = np.meshgrid(x, y)

Z = df["start_lng"]

fig, ax = plt.subplots(subplot_kw={'projection': "3d"})

ax.plot_surface(X, Y, Z, cmap="viridis")

plt.show()