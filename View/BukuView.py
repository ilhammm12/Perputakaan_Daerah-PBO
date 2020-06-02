from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


app = QApplication(sys.argv)

window = QWidget()
window.setGeometry(350,150,600,630)
window.setWindowTitle('Data Buku ')
window.setToolTip('This program is not complete')


Lable1 = QLabel('Nomor Rak :',window)
Lable1.move(10,15)
Lable2 = QLabel('Gendre Rak :',window)
Lable2.move(215,15)
Lable3 = QLabel('ID Buku :',window)
Lable3.move(10,65)
Lable4 = QLabel('Judul Buku :',window)
Lable4.move(215,65)
Lable4 = QLabel('Pengarang :',window)
Lable4.move(10,115)
Lable5 = QLabel('Penerbit :',window)
Lable5.move(10,165)
Lable6 = QLabel('Tahun Terbit :',window)
Lable6.move(10,215)
Lable6 = QLabel('Stok :',window)
Lable6.move(235,215)





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
LinEd1.resize(130,30)
LinEd1.move(80,10)
LinEd2 = QLineEdit('',window)
LinEd2.resize(150,30)
LinEd2.move(280,10)
LinEd3 = QLineEdit('',window)
LinEd3.resize(150,30)
LinEd3.move(60,60)
LinEd4 = QLineEdit('',window)
LinEd4.resize(150,30)
LinEd4.move(280,60)
LinEd5 = QLineEdit('',window)
LinEd5.resize(355,30)
LinEd5.move(75,110)
LinEd6 = QLineEdit('',window)
LinEd6.resize(365,30)
LinEd6.move(65,160)
LinEd7 = QLineEdit('',window)
LinEd7.resize(135,30)
LinEd7.move(80,210)
LinEd8 = QLineEdit('',window)
LinEd8.resize(158,30)
LinEd8.move(270,210)



tablEx = QTableWidget(window)
tablEx.resize(600,320 )
tablEx.move(10,270)
tablEx.setColumnCount(8)
tablEx.setRowCount(9)
tablEx.setHorizontalHeaderLabels(("Nomor Rak, Gendre Rak, ID Buku, Judul Buku, Pengarang, Penerbit, Tahun Terbit, Stok").split(','))



window.show()
app.exec_()
