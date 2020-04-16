class Superadmin:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def set_petugas(self,):
        return

    def set_username(self, value):
        self.username = value

    def set_password(self, value):
        self.password = value

class petugas():

    def __init__(self, id, nama, alamat, email, jeniskel, ):
        self.id_petugas = id
        self.nama_petugas = nama
        self.alamat = alamat
        self.email = email
        self.jenis_kelamin = jeniskel
        self.id_laporan = {}

    def getid_petugas(self) :
        return self.id_petugas

    def setid_petugas(self, id):
        self.id_petugas = id

    def getnama_petugas(self):
        return self.nama_petugas

    def setnama_petugas(self, nama):
        self.nama_petugas = nama

    def getalamat(self):
        return self.alamat

    def setalamat(self, alamat):
        self.alamat = alamat

    def getemail(self):
        return self.email

    def setemail(self, email):
        self.email = email

    def getjenis_kelamin(self):
        return self.jenis_kelamin

    def setjenis_kelamin (self, jeniskel):
        self.jenis_kelamin = jeniskel

    def getid_laporan(self):
        return self.id_laporan

    def setid_laporan(self, ):
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
