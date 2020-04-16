class Peminjaman:
    def __init__(self, id_pinjam, id_agt, id_ptg, id_buku, tanggalpinjam, tanggalkembali, status):
        self.id_pinjam = id_pinjam
        self.id_agt = id_agt
        self.id_ptg = id_ptg
        self.id_buku = id_buku
        self.tanggalpinjam = tanggalpinjam
        self.tanggalkembali = tanggalkembali

    def get_id_pinjam(self):
        return self.id_pinjam
    def set_id_pinjam(self, value):
        self.id_pinjam = value

    def get_id_agt(self):
        return self.id_agt
    def set_id_agt(self, value):
        self.id_agt = value

    def get_id_ptg(self):
        return self.id_ptg
    def set_id_ptg(self, value):
        self.id_ptg = value

    def get_id_buku(self):
        return self.id_buku
    def set_id_buku(self, value):
        self.id_buku = value

    def get_status(self):
        return self.status
    def set_status(self, value):
        self.status = value

class pengembalian() :

    def __init__(self, id, denda):
        self.id_pengembalian = id
        self.denda = denda

    def getid_pengembalian(self):
        return self.id_pengembalian

    def setid_pengembalian(self, id):
        self.id_pengembalian = id

    def getdenda(self):
        return self.denda

    def setdenda(self, denda):
        self.denda = denda
