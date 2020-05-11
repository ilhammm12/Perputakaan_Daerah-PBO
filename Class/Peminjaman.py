from Database.base import sessionFactory
from Database.ORM.OrmTransaksi import OrmTransaksi
from Anggota import Anggota
from Petugas import Petugas
from Buku import Buku

class Peminjaman:
    def __init__(self, Anggota, Petugas, Buku = [], tanggalPinjam, tanggalKembali, status):
        self.__Anggota = Anggota
        self.__Petugas = Petugas 
        self.__Buku = Buku
        self.__tanggalPinjam = tanggalPinjam
        self.__tanggalKembali = tanggalKembali
        self.__status = status

    @property
    def tanggalPinjam(self):
        return self.__tanggalPinjam
    @tanggalPinjam.setter
    def tanggalPinjam(self, value):
        self.__tanggalPinjam = value

    @property
    def tanggalKembalig(self):
        return self.__tanggalKembali
    @tanggalKembalig.setter
    def tanggalKembalig(self, value):
        self.__tanggalKembali = value

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, value):
        self.__status = value