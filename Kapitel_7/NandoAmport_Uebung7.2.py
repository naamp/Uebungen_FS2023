import matplotlib.pyplot as plt
import numpy as np

def f(x,y):
    return np.exp(-x**2) * np.sin(y)

#DEFINITION ACHSEN------------------------------------------------------------------
x = np.linspace(-4,4,200)
y = np.linspace(-4,4,200)

X, Y = np.meshgrid(x, y)
Z = f(X,Y)

#DEFINITION PLOT--------------------------------------------------------------------
plt.pcolormesh(X, Y, Z)
cb = plt.colorbar()
cb.set_label("Z-Werte")
plt.title("Funktion f(x,y) = exp(-x2) * sin(y)")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Random Punkte")
plt.grid(True)
plt.show()