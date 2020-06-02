from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


app = QApplication(sys.argv)

window = QWidget()
window.setGeometry(350,150,600,630)
window.setWindowTitle(' Data Anggota')
window.setToolTip('This program is not complete')


Lable1 = QLabel('No identitas :',window)
Lable1.move(10,15)
Lable2 = QLabel('No HP :',window)
Lable2.move(235,15)
Lable3 = QLabel('Nama :',window)
Lable3.move(10,65)
Lable4 = QLabel('Jenis Kelamin :',window)
Lable4.move(220,65)
Lable4 = QLabel('Tempat dan Tanggal Lahir :',window)
Lable4.move(10,115)
Lable5 = QLabel('Alamat:',window)
Lable5.move(10,165)
Lable6 = QLabel('Email :',window)
Lable6.move(10,215)
Lable6 = QLabel('Password :',window)
Lable6.move(220,215)





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
LinEd2.resize(165,30)
LinEd2.move(275,10)
LinEd3 = QLineEdit('',window)
LinEd3.resize(165,30)
LinEd3.move(50,60)

RadioM = QRadioButton('Laki-laki',window)
RadioM.move(295,62)
RadioF = QRadioButton('Perempuan',window)
RadioF.move(360,62)

LinEd5 = QLineEdit('',window)
LinEd5.resize(293,30)
LinEd5.move(145,110)
LinEd6 = QLineEdit('',window)
LinEd6.resize(385,30)
LinEd6.move(50,160)
LinEd7 = QLineEdit('',window)
LinEd7.resize(170,30)
LinEd7.move(45,210)
LinEd7 = QLineEdit('',window)
LinEd7.resize(160,30)
LinEd7.move(275,210)



tablEx = QTableWidget(window)
tablEx.resize(560,320 )
tablEx.move(10,270)
tablEx.setColumnCount(8)
tablEx.setRowCount(9)
tablEx.setHorizontalHeaderLabels(("No. Identitas, No. HP, Nama, Jenis Kelamin, TTL , Alamat, Email, Password").split(','))



window.show()
app.exec_()
