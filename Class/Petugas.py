from Database.base import sessionFactory
from Database.ORM.OrmPetugas import OrmPetugas
from JenisKelamin import JenisKelamin

class Petugas():

    def __init__(self, namaPetugas, tempatLahir, tanggalLahir, alamat, email, jenisKelamin):
        self.__namaPetugas = namaPetugas
        self.__tempatLahir = tempatLahir
        self.__tanggalLahir = tanggalLahir
        self.__alamat = alamat
        self.__email = email
        self.__jenisKelamin = jenisKelamin

        @property
        def namaPetugas(self):
            return self.__namaPetugas

        @namaPetugas.setter
        def namaPetugas(self, namaPetugas):
            self.__namaPetugas = namaPetugas

        @property
        def tempatLahir(self):
            return self.__tempatLahir

        @tempatLahir.setter
        def tempatLahir(self, tempatLahir):
            self.__tempatLahir = tempatLahir
         
        @property
        def tanggalLahir(self):
            return self.__tanggalLahir

        @tanggalLahir.setter
        def tanggalLahir(self, tanggalLahir):
            self.__tanggalLahir = tanggalLahir

        @property
        def alamat(self) :
            return self.__alamat

        @alamat.setter
        def alamat(self, alamat):
            self.__alamat = alamat

        @property
        def email(self):
            return self.__email

        @email.setter
        def email(self, email):
            self.__email = email

        @property
        def jenisKelamin(self):
            return self.__jenisKelamin

        @jenisKelamin.setter
        def jenisKelamin(self, jenisKelamin):
            self.__jenisKelamin = jenisKelamin
