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
    def __init__(self, id_laporan, jumlah_peminjaman, bulan_tahun, jumlah_pengunjung):
        self.id_laporan = id_laporan
        self.jumlah_peminjaman = jumlah_peminjaman
        self.bulan_tahun = bulan_tahun
        self.jumlah_pengunjung = jumlah_pengunjung

    def get_id_laporan(self):
        return self.id_laporan

    def set_id_laporan(self, id_laporan):
        self.id_laporan = id_laporan

    def get_jumlah_peminjaman(self):
        return self.jumlah_peminjaman

    def set_jumlah_peminjaman(self, jumlah_peminjaman):
        self.jumlah_peminjaman = jumlah_peminjaman

    def get_bulan_tahun(self):
        return self.bulan_tahun

    def set_bulan_tahun(self, bulan_tahun):
        self.bulan_tahun = bulan_tahun

    def get_jumlah_pengunjung(self):
        return self.jumlah_pengunjung

    def set_jumlah_pengunjung(self, jumlah_pengunjung):
        self.jumlah_pengunjung = jumlah_pengunjung
