class Superadmin:

    def __init__(self, *args, **kwargs):
        self.__username = kwargs.get('username','admin')
        self.__password = kwargs.get('password','admin321')

    def set_petugas(self,):
        return

    def username(self, value):
        self.__username = value

    def password(self, value):
        self.__password = value

class petugas():

    def __init__(self, *args, **kwargs ):
        self.id_petugas = kwargs.get ('id_petugas', 'PS0001')
        self.nama_petugas = kwargs.get ('nama_petugas', 'Dwianti')
        self.alamat = kwargs.get ('alamat', 'jl.Setia Budi')
        self.email = kwargs.get ('emai', 'dwianti123@gmail.com')
        self.jenis_kelamin = kwargs.get ('jenis_kelamin', 'perempuan')
        self.id_laporan = {}

    @property
    def id_petugas(self) :
        return self.id_petugas
    @id_petugas.setter
    def id_petugas(self, id):
        self.id_petugas = id

    @property
    def nama_petugas(self):
        return self.nama_petugas
    @nama_petugas.setter
    def nama_petugas(self, nama):
        self.nama_petugas = nama

    @property
    def alamat(self):
        return self.alamat
    @alamat.setter
    def alamat(self, alamat):
        self.alamat = alamat

    @property
    def email(self):
        return self.email
    @email.setter
    def email(self, email):
        self.email = email

    @property
    def jenis_kelamin(self):
        return self.jenis_kelamin
    @jenis_kelamin.setter
    def jenis_kelamin (self, jeniskelamin):
        self.jenis_kelamin = jeniskelamin

    @property
    def id_laporan(self):
        return self.id_laporan 
    @id_laporan.setter
    def id_laporan(self, ):
        self.id_laporan = {}

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
        
