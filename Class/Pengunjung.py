class Pengunjung():

    def __init__(self, nama, alamat, nomorTelpon, pencarian):
        self.__nama = nama
        self.__alamat = alamat
        self.__nomorTelpon = nomorTelpon
        self.__pencarian = pencarian

    @property
    def pencarian(self):
        return self.__pencarian

    @pencarian.setter
    def pencarian(self, ):
        self.__pencarian = pencarian
