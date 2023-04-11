import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import urllib.parse 
query = 'Hellö Wörld@' 
a = urllib.parse.quote(query)

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
        self.land.addItems(["Schweiz", "Deutschland", "Österreich"])
        
        self.button2 = QPushButton("Auf Karte anzeigen")
        self.button3 = QPushButton("Laden")
        self.button1 = QPushButton("Speichern")

        # Widgets dem Layout hinzufügen:------------------------------------------------------------------------------
        # Layout füllen: 
        layout.addRow("Vorname:", self.vorname) 
        layout.addRow("Name:", self.name) 
        layout.addRow("Geburtstag:", self.geburtstag)
        layout.addRow("Adresse:", self.adresse) 
        layout.addRow("Postleitzahl:", self.plz)
        layout.addRow("Ort:", self.ort)
        layout.addRow("Land:", self.land)
        layout.addRow(self.button2)
        layout.addRow(self.button3)
        layout.addRow(self.button1)

        # Menubar erstellen:-----------------------------------------------------------------------------------------
        menubar = self.menuBar()
        filemenu = menubar.addMenu("File")
        
        self.save = QAction("Save", self)
        self.quit = QAction("Quit", self)
        self.laden = QAction("Load", self)

        filemenu.addAction(self.save)
        filemenu.addAction(self.laden)
        filemenu.addAction(self.quit)
        


        viewmenu = menubar.addMenu("View")
        self.karte = QAction("Karte", self)

        viewmenu.addAction(self.karte)

        # Aktionen:--------------------------------------------------------------------------------------------------
        self.button1.clicked.connect(self.Datensicherung)
        self.save.triggered.connect(self.Datensicherung)
        self.quit.triggered.connect(self.selfdestruct)

        self.button2.clicked.connect(self.Anzeige_Karte)
        self.karte.triggered.connect(self.Anzeige_Karte)
        self.button3.clicked.connect(self.Daten_laden)
        self.laden.triggered.connect(self.Daten_laden)

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

        filename, filter = QFileDialog.getSaveFileName(self, "Datei speichern", "", "Text Datei (*.txt)")

        file = open(filename, "w")

        v = self.vorname.text()
        n = self.name.text()
        g = self.geburtstag.text()
        a = self.adresse.text()
        p = self.plz.text()
        o = self.ort.text()
        c = self.land.currentText()

        text = v+","+n+","+g+","+a+","+p+","+o+","+c
        file.write(text)
        
        file.close()

        print("Die Daten wurden gesichert")

    def Anzeige_Karte(self):

        a = self.adresse.text()
        o = self.ort.text()
        c = self.land.currentText()

        pfad = f"https://www.google.ch/maps/place/{a}/{o}/{c}"

        QDesktopServices.openUrl(QUrl(pfad))

        print("Google Maps wurde geöffnet")

    def Daten_laden(self):
        filename, filter = QFileDialog.getOpenFileName(self, "Datei laden", "", "Text Files (*.txt) ;; Python Files (*.py)")

       
        file = open(filename, "r", encoding= "utf-8")
        data = file.read().split(",")
        self.vorname.setText(data[0])
        self.name.setText(data[1])
        self.geburtstag.setDate(QDate.fromString(data[2], "dd.MM.yyyy"))
        self.adresse.setText(data[3])
        self.plz.setText(data[4])
        self.ort.setText(data[5])
        self.land.setCurrentText(data[6])
                
        print("File geladen")
        


def main():
    app = QApplication(sys.argv)  # Qt Applikation erstellen
    mainwindow = MyWindow()       # Instanz Fenster erstellen
    mainwindow.raise_()           # Fenster nach vorne bringen
    app.exec_()                   # Applikations-Loop starten

if __name__ == '__main__':
    main()