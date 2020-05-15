import sys
from PyQt5 import QtGui
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import QApplication, QGridLayout, QMessageBox, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.title = "Anggota"
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
        self.tableWidget.setItem(0, 2, QTableWidgetItem("Telpon"))
        self.tableWidget.setItem(0, 3, QTableWidgetItem("Tempat lahir"))
        self.tableWidget.setItem(0, 4, QTableWidgetItem("Tanggal lahir"))
        self.tableWidget.setItem(0, 5, QTableWidgetItem("Status"))
        # self.tableWidget.setColumnWidth(1, 200)

        self.tableWidget.setItem(1, 0, QTableWidgetItem("Parwiz"))
        self.tableWidget.setItem(1, 1, QTableWidgetItem("Kemakmuran"))
        self.tableWidget.setItem(1, 2, QTableWidgetItem("845845845"))
        self.tableWidget.setItem(1, 3, QTableWidgetItem("Balikpapan"))
        self.tableWidget.setItem(1, 4, QTableWidgetItem("30 Juli 2000"))
        self.tableWidget.setItem(1, 5, QTableWidgetItem("aktif"))

        self.tableWidget.setItem(2, 0, QTableWidgetItem("Rizal"))
        self.tableWidget.setItem(2, 1, QTableWidgetItem("Kebaktian"))
        self.tableWidget.setItem(2, 2, QTableWidgetItem("912392245"))
        self.tableWidget.setItem(2, 3, QTableWidgetItem("Balikpapan"))
        self.tableWidget.setItem(2, 4, QTableWidgetItem("1 Agustus 2000"))
        self.tableWidget.setItem(2, 5, QTableWidgetItem("aktif"))


        self.tableWidget.setItem(3, 0, QTableWidgetItem("Bakri"))
        self.tableWidget.setItem(3, 1, QTableWidgetItem("Sambutan"))
        self.tableWidget.setItem(3, 2, QTableWidgetItem("21394212"))
        self.tableWidget.setItem(3, 2, QTableWidgetItem("Balikpapan"))
        self.tableWidget.setItem(3, 2, QTableWidgetItem("5 April 2000"))
        self.tableWidget.setItem(3, 2, QTableWidgetItem("aktif"))


        self.vBoxLayout = QVBoxLayout()
        self.vBoxLayout.addWidget(self.tableWidget)
        self.setLayout(self.vBoxLayout)


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
