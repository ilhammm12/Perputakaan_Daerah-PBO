class laporan():
  
    def __init__(self, *args, **kwargs):
        self.__id_laporan = kwargs.get('id_laporan', '0001') 
        self.__jumlah_peminjaman = kwargs.get('jumlah_peminjaman', '14') 
        self.__bulan_tahun= kwargs.get('bulan_tahun', 'Maret 2020') 
        self.__jumlah_pengunjung = kwargs.get('jumlah_pengunjung', '87') 
        
    @property
    def id_laporan(self):
        return self.__id_laporan
       
    @id_laporan.setter
    def id_laporan(self, id_laporan):
        self.__id_laporan = id_laporan
       
    @property
    def jumlah_peminjaman(self):
        return self.__jumlah_peminjaman
        
    @jumlah_peminjaman.setter
    def jumlah_peminjaman(self, jumlah_peminjaman):
        self.__jumlah_peminjaman = jumlah_peminjaman
        	
    @property
    def bulan_tahun(self):
        return self.__bulan_tahun
        
    @bulan_tahun.setter
    def bulan_tahun(self, bulan_tahun):
        self.__bulan_tahun = bulan_tahun
        	
    @property
    def jumlah_pengunjung(self):
        return self.__jumlah_pengunjung
        
    @jumlah_pengunjung.setter
    def jumlah_pengunjung(self, jumlah_pengunjung):
        self.__jumlah_pengunjung = jumlah_pengunjung