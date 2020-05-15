import sys
from PyQt5 import QtGui
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import QApplication, QGridLayout, QMessageBox, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.title = "Petugas"
        self.top = 100
        self.left = 100
        self.width = 700
        self.height = 500

        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)

        self.creatingTables()

        self.show()

    def creatingTables(self):
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(6)

        self.tableWidget.setItem(0, 0, QTableWidgetItem("Name"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("Alamat"))
        self.tableWidget.setItem(0, 3, QTableWidgetItem("Tempat lahir"))
        self.tableWidget.setItem(0, 4, QTableWidgetItem("Tanggal lahir"))
        self.tableWidget.setItem(0, 5, QTableWidgetItem("Email"))
        self.tableWidget.setItem(0, 5, QTableWidgetItem("Jenis Kelamin"))
        # self.tableWidget.setColumnWidth(1, 200)

        self.tableWidget.setItem(1, 0, QTableWidgetItem("Parwiz"))
        self.tableWidget.setItem(1, 1, QTableWidgetItem("Gg Sari"))
        self.tableWidget.setItem(1, 3, QTableWidgetItem("Balikpapan"))
        self.tableWidget.setItem(1, 2, QTableWidgetItem("22 Apr 2000"))
        self.tableWidget.setItem(1, 4, QTableWidgetItem("Budi223@gmail.com"))
        self.tableWidget.setItem(1, 5, QTableWidgetItem("Lakilaki"))

        self.tableWidget.setItem(2, 0, QTableWidgetItem("Badrun"))
        self.tableWidget.setItem(2, 1, QTableWidgetItem("Kebun Sayur"))
        self.tableWidget.setItem(2, 3, QTableWidgetItem("Balikpapan"))
        self.tableWidget.setItem(2, 2, QTableWidgetItem("25 Apr 2000"))
        self.tableWidget.setItem(2, 4, QTableWidgetItem("badrun253@gmail.com"))
        self.tableWidget.setItem(2, 5, QTableWidgetItem("Lakilaki"))

        self.vBoxLayout = QVBoxLayout()
        self.vBoxLayout.addWidget(self.tableWidget)
        self.setLayout(self.vBoxLayout)


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())