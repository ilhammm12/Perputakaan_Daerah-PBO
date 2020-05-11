from Class.Registrasi import Registrasi
from Database.base import sessionFactory
from Database.ORM.OrmAnggota import OrmAnggota

class Anggota:

    def __init__(self, nama, alamat, telpon, tempatLahir,tanggalLahir):
        self.__nama = nama
        self.__alamat = alamat
        self.__telpon = telpon
        self.__tempatLahir = tempatLahir
        self.__tanggalLahir = tanggalLahir
        self.__status = status

    def GetPencarian(self,):
        return

    @property
    def nama(self):
        return self.__nama
    @nama.setter
    def nama(self, value):
        self.__nama = value

    @property
    def alamat(self):
        return self.__alamat
    @alamat.setter
    def alamat(self, value):
        self.__alamat = value

    @property
    def telpon(self):
        return self.__telpon
    @telpon.setter
    def telpon(self, value):
        self.__telpon = value

    @property
    def tempatLahir(self):
        return self.__tempatLahir
    @tempatLahir.setter
    def tempatLahir(self, value):
        self.__tempatLahir = value

    @property
    def tanggalLahir(self):
        return self.__tanggalLahir
    @tanggalLahir.setter
    def tanggalLahir(self, value):
        self.__tanggalLahir = value

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, value):
        self.__status = value
