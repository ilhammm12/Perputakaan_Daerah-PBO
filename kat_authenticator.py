class login():

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def get_username(self):
        return self.username

    def set_username(self, username):
        self.username = username

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password

class registrasi():

    def __init__(self, no_regis, nik, nama, tempat_lahir, tgl_lahir, alamat, no_hp, jenis_kelamin, jenis_anggota):
        self.no_regis = no_regis
        self.nik = nik
        self.nama = nama
        self.tempat_lahir = tempat_lahir
        self.tgl_lahir = tgl_lahir
        self.alamat = alamat
        self.no_hp = no_hp
        self.jenis_kelamin = jenis_kelamin
        self.jenis_anggota = jenis_anggota

    def get_no_regis(self):
        return self.no_regis

    def set_no_regis(self, no_regis):
        self.no_regis = no_regis

    def get_nik(self):
        return self.nik

    def set_nik(self, nik):
        self.nik = nik

    def get_nama(self):
        return self.nama

    def set_nama(self, nama):
        self.nama = nama

    def get_tempat_lahir(self):
        return self.tempat_lahir

    def set_tempat_lahir(self, tempat_lahir):
        self.tempat_lahir = tempat_lahir

    def get_tgl_lahir(self):
        return self.tgl_lahir

    def set_tgl_lahir(self, tgl_lahir):
        self.tgl_lahir = tgl_lahir

    def get_alamat(self):
        return self.alamat

    def set_alamat(self, alamat):
        self.alamat = alamat

    def get_no_hp(self):
        return self.no_hp

    def set_no_hp(self, no_hp):
        self.no_hp = no_hp

    def get_jenis_kelamin(self):
        return self.jenis_kelamin

    def set_jenis_kelamin(self, jenis_kelamin):
        self.jenis_kelamin = jenis_kelamin

    def get_jenis_anggota(self):
        return self.jenis_anggota

    def set_jenis_anggota(self, jenis_anggota):
        self.jenis_anggota = jenis_anggota
