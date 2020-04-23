class rak_buku():

    def __init__(self, *args, **kwargs):
        self.__nomor_rak = kwargs.get('nomor_rak', '12')
        self.__genre_rak = kwargs.get('genre', 'komik')

    @property
    def no_rak(self):
        return self.__nomor_rak

    @no_rak.setter
    def no_rak(self, nomor_rak):
        self.__nomor_rak = nomor_rak

    @property
    def genre_rak(self):
        return self.__genre_rak

    @genre_rak.setter
    def genre_rak(self, genre_rak):
        self.__genre_rak = genre_rak

class buku():

    def __init__(self, *args, **kwargs):
        self.__id_buku = kwargs.get('id_buku', '1234')
        self.__judul_buku = kwargs.get('judul_buku', 'Haliday')
        self.__pengarang = kwargs.get('pengarang', 'albert')
        self.__penerbit = kwargs.get('penerbit', 'jogjastore')
        self.__tahun_terbit = kwargs.get('tahun_ternit', '2005')
        self.__stok_buku = kwargs.get('stok_buku', '50')
        self.__nomor_rak = kwargs.get('nomor_rak', '12')

    @property
    def id_buku(self):
        return self.__id_buku

    @id_buku.setter
    def id_buku(self, id_buku):
        self.__id_buku = id_buku

    @property
    def judul_buku(self):
        return self.__judul_buku

    @judul_buku.setter
    def judul_buku(self, judul_buku):
        self.__judul_buku = judul_buku

    @property
    def pengarang(self):
        return self.__pengarang

    @pengarang.setter
    def pengarang(self, pengarang):
        self.__pengarang = pengarang

    @property
    def penerbit(self):
        return self.__penerbit

    @penerbit.setter
    def penerbit(self, penerbit):
        self.__penerbit = penerbit

    @property
    def tahun_terbit(self):
        return self.__tahun_terbit

    @tahun_terbit.setter
    def tahun_penerbit(self, tahun_terbit):
        self.__tahun_terbit = tahun_terbit

    @property
    def stok(self):
        return self.__stok_buku

    @stok.setter
    def stok(self, stok_buku):
        self.__stok_buku = stok_buku

    @property
    def no_rak(self):
        return self.__nomor_rak

    @no_rak.setter
    def no_rak(self, nomor_rak):
        self.__nomor_rak = nomor_rak

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
