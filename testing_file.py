import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df = pd.read_csv("Rides.csv", sep=",", header=0)
plt.hist(df["member_casual"])
plt.show()
