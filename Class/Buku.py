from Database.base import sessionFactory
from Database.ORM.OrmBuku import OrmBuku
from RakBuku import RakBuku

class Buku():

    def __init__(self, judulBuku, pengarang, penerbit, tahunTerbit, stokBuku, nomorRak):
        self.__judulBuku = judulBuku
        self.__pengarang = pengarang
        self.__penerbit = penerbit
        self.__tahunTerbit = tahunTerbit
        self.__stokBuku = stokBuku
        self.__nomorRak = nomorRak

    @property
    def judulBuku(self):
        return self.__judulBuku

    @judulBuku.setter
    def judulBuku(self, judulBuku):
        self.__judulBuku = judulBuku

    @property
    def pengarang(self):
        return self.__pengarang

    @pengarang.setter
    def pengarang(self, pengarang):
        self.__pengarang = pengarang

    @property
    def penerbit(self):
        return self.__penerbit

    @penerbit.setter
    def penerbit(self, penerbit):
        self.__penerbit = penerbit

    @property
    def tahunTerbit(self):
        return self.__tahunTerbit

    @tahunTerbit.setter
    def tahun_penerbit(self, tahunTerbit):
        self.__tahunTerbit = tahunTerbit

    @property
    def stokBuku(self):
        return self.__stokBuku

    @stokBuku.setter
    def stokBuku(self, stokBuku):
        self.__stokBuku = stokBuku

    @property
    def nomorRak(self):
        return self.__nomorRak

    @nomorRak.setter
    def nomorRak(self, nomorRak):
        self.__nomorRak = nomorRak
