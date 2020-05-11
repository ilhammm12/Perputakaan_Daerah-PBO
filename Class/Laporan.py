from Database.base import sessionFactory
from Database.ORM.OrmLaporan import OrmLaporan

class Laporan():
  
    def __init__(self, jumlahPeminjaman, bulan, tahun, jumlahPengunjung): 
        self.__jumlahPeminjaman = jumlahPeminjaman  
        self.__bulan = bulan
        self.__tahun = tahun
        self.__jumlahPengunjung = jumlahPengunjung  
    
    @property
    def jumlahPeminjaman(self):
        return self.__jumlahPeminjaman
        
    @jumlahPeminjaman.setter
    def jumlahPeminjaman(self, jumlahPeminjaman):
        self.__jumlahPeminjaman = jumlahPeminjaman
        	
    @property
    def bulan(self):
        return self.__bulan
        
    @bulan.setter
    def bulan(self, bulan):
        self.__bulan = bulan

    @property
    def tahun(self):
        return self.__tahun
        
    @tahun.setter
    def tahun(self, tahun):
        self.__bulan = tahun
        	
    @property
    def jumlahPengunjung(self):
        return self.__jumlahPengunjung
        
    @jumlahPengunjung.setter
    def jumlahPengunjung(self, jumlahPengunjung):
        self.__jumlahPengunjung = jumlahPengunjung