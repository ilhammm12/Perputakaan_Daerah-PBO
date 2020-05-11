from Anggota import Anggota
from Buku import Buku

class Pencarian():
    def __init__(self, Anggota, Buku, kataKunci, tanggalPencarian):
        self.Anggota = Anggota
        self.Buku = Buku
        self.kataKunci = kataKunci
        self.tanggalPencarian = tanggalPencarian
