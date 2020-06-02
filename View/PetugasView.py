from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


app = QApplication(sys.argv)

window = QWidget()
window.setGeometry(350,150,600,630)
window.setWindowTitle(' Data Petugas')
window.setToolTip('This program is not complete')


Lable1 = QLabel('ID Petugas :',window)
Lable1.move(10,15)
Lable2 = QLabel('Nama :',window)
Lable2.move(235,15)
Lable3 = QLabel('Jenis Kelamin :',window)
Lable3.move(10,65)
Lable4 = QLabel('Tempat dan Tanggal Lahir :',window)
Lable4.move(10,115)
Lable5 = QLabel('Alamat:',window)
Lable5.move(240,65)
Lable6 = QLabel('Email :',window)
Lable6.move(10,165)





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
LinEd1.resize(150,30)
LinEd1.move(80,10)
LinEd2 = QLineEdit('',window)
LinEd2.resize(150,30)
LinEd2.move(275,10)
RadioM = QRadioButton('Laki-laki',window)
RadioM.move(85,63)
RadioF = QRadioButton('Perempuan',window)
RadioF.move(150,63)
LinEd5 = QLineEdit('',window)
LinEd5.resize(145,30)
LinEd5.move(280,60)
LinEd6 = QLineEdit('',window)
LinEd6.resize(280,30)
LinEd6.move(144,110)
LinEd7 = QLineEdit('',window)
LinEd7.resize(380,30)
LinEd7.move(45,160)




tablEx = QTableWidget(window)
tablEx.resize(560,320 )
tablEx.move(10,220)
tablEx.setColumnCount(6)
tablEx.setRowCount(9)
tablEx.setHorizontalHeaderLabels(("ID Petugas, Nama, Jenis Kelamin, TTL , Alamat, Email").split(','))



window.show()
app.exec_()
