from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


app = QApplication(sys.argv)

window = QWidget()
window.setGeometry(350,150,600,630)
window.setWindowTitle(' Data Pinjam Buku')
window.setToolTip('This program is not complete')


Lable1 = QLabel('Nama Anggota:',window)
Lable1.move(10,15)
Lable2 = QLabel('Judul Buku :',window)
Lable2.move(10,65)
Lable3 = QLabel('Jumlah :',window)
Lable3.move(265,65)





btnAdd = QPushButton('Tambah',window)
btnAdd.resize(90,40)
btnAdd.move(480,30)

btnAdd2 = QPushButton('Ubah',window)
btnAdd2.resize(90,40)
btnAdd2.move(480,75)

btnAdd3 = QPushButton('Hapus',window)
btnAdd3.resize(90,40)
btnAdd3.move(480,120)


LinEd1 = QLineEdit('',window)
LinEd1.resize(350,30)
LinEd1.move(90,10)
LinEd2 = QLineEdit('',window)
LinEd2.resize(180,30)
LinEd2.move(75,60)
LinEd3 = QLineEdit('',window)
LinEd3.resize(130,30)
LinEd3.move(310,60)



tablEx = QTableWidget(window)
tablEx.resize(560,320 )
tablEx.move(10,190)
tablEx.setColumnCount(3)
tablEx.setRowCount(9)
tablEx.setHorizontalHeaderLabels(("Nama Anggota, Judul Buku, Jumlah").split(','))



window.show()
app.exec_()
