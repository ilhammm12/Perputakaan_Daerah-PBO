from Database.base import sessionFactory
from Database.ORM.OrmRegistrasi import OrmRegistrasi
from JenisKelamin import JenisKelamin

class Registrasi():

    def __init__(self, nik, nama, tempatLahir, tanggalLahir, alamat, noTelpon, jenisKelamin, JenisAnggota):
        self.__nik = nik
        self.__nama = nama
        self.__tempatLahir = tempatLahir
        self.__tanggalLahir = tanggalLahir
        self.__alamat = alamat
        self.__noTelpon = noTelpon
        self.__jenisKelamin = jenisKelamin
        self.__jenisAnggota = JenisAnggota 

    @property
    def nik(self):
        return self.__nik
        
    @nik.setter
    def nik(self, nik):
        self.__nik = nik
        
    @property
    def nama(self):
        return self.__nama
        
    @nama.setter
    def nama(self, nama):
        self.__nama = nama
        
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
    def alamat(self):
        return self.__alamat
        
    @alamat.setter
    def alamat(self, alamat):
        self.__alamat = alamat
   
    @property
    def noTelpon(self):
        return self.__noTelpon
        
    @noTelpon.setter
    def noTelpon(self, noTelpon):
        self.__noTelpon = noTelpon  
        
    @property
    def jenisKelamin(self):
        return self.__jenisKelamin
      
    @jenisKelamin.setter
    def jenisKelamin(self, jenisKelamin):
        self.__jenisKelamin = jenisKelamin
        
    @property
    def jenisAnggota(self):
        return self.__jenisAnggota
       
    @jenisAnggota.setter
    def jenisAnggota(self, jenisAnggota):
        self.__jenisAnggota = jenisAnggota              	