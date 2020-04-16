class pengunjung():

    def __init__(self, nama, almt, tlp, jum_peng, ):
        self.nama = nama
        self.alamat = almt
        self.nomor_telepon = tlp
        self.jumlah_pengunjung = jum_peng
        self.pencarian = {}

    def get_pencarian(self):
        return self.pencarian

    def set_pencarian(self, ):
        self.pencarian

class Anggota:

    def __init__(self, id,nama, alamat, telpon, tempatlahir, tanggallahir, status):
        self.id = id
        self.nama = nama
        self.alamat = alamat
        self.telpon = telpon
        self.tempatlahir = tempatlahir
        self.tanggallahir = tanggallahir
        self.status = status

    def GetPencarian(self,):
        return

    def get_id(self):
        return self.id
    def set_id(self, value):
        self.id = value

    def get_nama(self):
        return self.nama
    def set_nama(self, value):
        self.nama = value

    def get_alamat(self):
        return self.alamat
    def set_alamat(self, value):
        self.alamat = value

    def get_telpon(self):
        return self.telpon
    def set_telpon(self, value):
        self.telpon = value

    def get_tempatlahir(self):
        return self.tempatlahir
    def set_tempatlahir(self, value):
        self.tempatlahir = value

    def get_tanggallahir(self):
        return self.tanggallahir
    def set_tanggallahir(self, value):
        self.tanggallahir = value

    def get_status(self):
        return self.status
    def set_status(self, value):
        self.status = value



