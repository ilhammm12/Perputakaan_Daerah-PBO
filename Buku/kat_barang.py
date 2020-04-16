class rak_buku():

    def __init__(self, no_rak, genre):
        self.nomor_rak = no_rak
        self.genre_rak = genre

    def get_no_rak(self):
        return self.nomor_rak

    def set_no_rak(self, nomor_rak):
        self.nomor_rak

    def get_genre_rak(self):
        return self.genre_rak

    def set_genre_rak(self, genre_rak):
        self.genre_rak

class buku():

    def __init__(self, id, judul, pengarang, penerbit, thn, stok, rak):
        self.id_buku = id
        self.judul_buku = judul
        self.pengarang = pengarang
        self.penerbit = penerbit
        self.tahun_terbit = thn
        self.stok_buku = stok
        self.nomor_rak = rak

    def get_id_buku(self):
        return self.id_buku

    def set_id_buku(self, id_buku):
        self.id_buku

    def get_judul_buku(self):
        return self.judul_buku

    def set_judul_buku(self, judul_buku):
        self.judul_buku

    def get_pengarang(self):
        return self.pengarang

    def set_pengarang(self, pengarang):
        self.pengarang

    def get_penerbit(self):
        return self.penerbit

    def set_penerbit(self, penerbit):
        self.penerbit

    def get_tahun(self):
        return self.tahun_terbit

    def set_tahun(self, tahun_terbit):
        self.tahun_terbit

    def get_stok(self):
        return self.stok_buku

    def set_stok(self, stok_buku):
        self.stok_buku

    def get_no_rak(self):
        return self.nomor_rak

    def set_no_rak(self, nomor_rak):
        self.nomor_rak
