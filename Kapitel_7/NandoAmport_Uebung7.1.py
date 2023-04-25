import matplotlib.pyplot as plt
import matplotlib.pyplot as patches
from math import sin, pi
import numpy as np



# DEFINITION ACHSEN------------------------------------------------------------------
x = np.random.random(1000)
x = x*200-100

y = np.random.random(1000)
y = y*200-100

# DEFINITION Farbe-------------------------------------------------------------------

colors = np.random.rand(1000)
print(colors)

# DEFINITION PLOT--------------------------------------------------------------------

plt.scatter(x, y, c=colors)
#plt.plot(x, y, color=(1, 0, 0))  
plt.xlabel("x")
plt.ylabel("y")
plt.title("Random Punkte")
plt.grid(True)
plt.axis("equal")
plt.show()