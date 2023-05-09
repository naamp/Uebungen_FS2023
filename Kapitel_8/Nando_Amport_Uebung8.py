from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget
from PyQt5.uic import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("Kapitel_8\GUI_Uebung8.ui", self)
        self.show()

        figure = plt.figure(figsize=(16,9))
        self.canvas = FigureCanvas(figure)
        #self.verticalLayout.removeWidget(self.widget)
        self.verticalLayout.insertWidget(0, self.canvas)

        self.button1.clicked.connect(self.plot)
    


    def plot(self):
        plt.clf()   # clf ====== clear figure
        x = np.linspace(-5, 5, 20)
        y = x**2
        plt.plot(x,y,"bo-")
        plt.axis("equal")
        self.canvas.draw()

    def plot2(self):
        plt.clf()
        x = np.linspace(-2*np.pi, 2*np.pi, 20)
        y = np.sin(x)
        plt.plot(x,y,"ko-")
        plt.axis("equal")
        self.canvas.draw()

    def updateslider(self, value):
        plt.clf()
        x = np.linspace(-np.pi, np.pi, value)
        y = np.cos(x+value/80)
        y2 = np.cos(x)
        plt.plot(x,y, "go-")
        plt.plot(x,y2, "ro-")
        plt.axis("equal")
        self.canvas.draw()

app = QApplication([])
window = Window()
app.exec()

