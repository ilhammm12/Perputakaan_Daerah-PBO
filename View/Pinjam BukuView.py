from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


app = QApplication(sys.argv)

window = QWidget()
window.setGeometry(350,150,600,630)
window.setWindowTitle(' Data Peminjaman-Pengembalian Buku')
window.setToolTip('This program is not complete')


Lable1 = QLabel('Nama Anggota:',window)
Lable1.move(10,15)
Lable2 = QLabel('Judul Buku :',window)
Lable2.move(10,65)
Lable3 = QLabel('Jumlah :',window)
Lable3.move(265,65)
Lable4 = QLabel('Tanggal Peminjaman :',window)
Lable4.move(10,115)
Lable5 = QLabel('Tanggal Pengembalian :',window)
Lable5.move(10,165)
Lable6 = QLabel('Status :',window)
Lable6.move(295,165)





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
LinEd4 = QLineEdit('',window)
LinEd4.resize(320,30)
LinEd4.move(120,110)
LinEd5 = QLineEdit('',window)
LinEd5.resize(155,30)
LinEd5.move(130,155)
LinEd6 = QLineEdit('',window)
LinEd6.resize(105,30)
LinEd6.move(335,155)



tablEx = QTableWidget(window)
tablEx.resize(560,320 )
tablEx.move(10,215)
tablEx.setColumnCount(6)
tablEx.setRowCount(9)
tablEx.setHorizontalHeaderLabels(("Nama Anggota, Judul Buku, Jumlah, tgl pinjam, tgl kembali, status").split(','))



window.show()
app.exec_()
