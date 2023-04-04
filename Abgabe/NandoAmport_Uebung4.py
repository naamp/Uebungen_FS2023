import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Fenster-Titel definieren:
        self.setWindowTitle("GUI-Programmierung")

        # Layout erstellen:
        layout = QFormLayout()

        # Widget-Instanzen erstellen:--------------------------------------------------------------------------------
        self.vorname = QLineEdit()
        self.name = QLineEdit()
        self.geburtstag = QDateEdit()
        self.adresse = QLineEdit()
        self.plz = QLineEdit()
        self.ort = QLineEdit()
        self.land = QComboBox()
        self.button1 = QPushButton("save")

        # Widgets dem Layout hinzufügen:------------------------------------------------------------------------------
        # Layout füllen: 
        layout.addRow("Vorname:", self.vorname) 
        layout.addRow("Name:", self.name) 
        layout.addRow("Geburtstag:", self.geburtstag)
        layout.addRow("Adresse:", self.adresse) 
        layout.addRow("Postleitzahl:", self.plz)
        layout.addRow("Ort:", self.ort)
        layout.addRow("Land:", self.land)
        layout.addRow(self.button1)

        # Menubar erstellen:-----------------------------------------------------------------------------------------
        menubar = self.menuBar()
        filemenu = menubar.addMenu("File")

        self.save = QAction("Save", self)
        self.quit = QAction("Quit", self)

        filemenu.addAction(self.save)
        filemenu.addAction(self.quit)

        self.land.addItems(["Schweiz", "Deutschland", "Österreich"])

        # Aktionen:--------------------------------------------------------------------------------------------------
        self.button1.clicked.connect(self.Datensicherung)
        self.save.triggered.connect(self.Datensicherung)
        self.quit.triggered.connect(self.selfdestruct)

        # Zentrales Widget erstellen und layout hinzufügen:----------------------------------------------------------
        center = QWidget()
        center.setLayout(layout)

        # Zentrales Widget in diesem Fenster setzen
        self.setCentralWidget(center)

        # Fenster anzeigen
        self.show()


 # Funktionen definieren:--------------------------------------------------------------------------------------------

    def selfdestruct(self):
        self.close()
        print("Das Fenster wurde geschlossen!")

    def Datensicherung(self):

        file = open("output.txt", "w")

        text = self.vorname.text()+","+self.name.text()+","+self.geburtstag.text()+","+self.adresse.text()+","+self.ort.text()+","+self.land.currentText()
        file.write(text)
        
        file.close()


        print("Die Daten wurden gesichert")




def main():
    app = QApplication(sys.argv)  # Qt Applikation erstellen
    mainwindow = MyWindow()       # Instanz Fenster erstellen
    mainwindow.raise_()           # Fenster nach vorne bringen
    app.exec_()                   # Applikations-Loop starten

if __name__ == '__main__':
    main()