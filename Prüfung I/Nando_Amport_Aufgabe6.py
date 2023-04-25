from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Währungsumrechner")

        #layout erzeugen
        #layout = ... # QVBoxLayout, QHBoxLayout, QGridlayout, ...
        layout = QFormLayout()


        #gui Elemente erstellen

        self.CHF = QLineEdit()
        self.Euro = QLabel()
        
      
        self.umrechnung_button = QPushButton("Umrechnen")
     
        #gui Elemente dem Layout hinzufügen

        layout.addRow("Schweizer Franken:", self.CHF)
        layout.addRow("Euro:", self.Euro)
        layout.addRow(self.umrechnung_button)

        #Connect

        self.umrechnung_button.clicked.connect(self.CHF_to_Euro)

        #Fenster öffnen
        center = QWidget()
        center.setLayout(layout)

        self.setCentralWidget(center)

        self.show()

    #Funktionen

    def CHF_to_Euro(self):
        self.Euro.setText(str(""))
        try:
            self.CHF = float(self.CHF.text())
            self.Euro_res = 0.8760 * self.CHF
            self.Euro.setText(str(self.Euro_res))
            
        except:
            QMessageBox.warning(self,"Achtung", "Sie müssen eine Zahl eingeben!!!")

app = QApplication([])
win = Fenster()
app.exec()