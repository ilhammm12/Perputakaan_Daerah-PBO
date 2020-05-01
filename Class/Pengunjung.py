class pengunjung():

    def __init__(self, *args, **kwargs):
        self.__nama = kwargs.get('nama', 'wahyu')
        self.__alamat = kwargs.get('alamat', 'jln baturatna KM 11 ')
        self.__nomor_telepon = kwargs.get('nomor_telpon', '083141124872')
        self.__jumlah_pengunjung = kwargs.get('jumlah_pengunjung', '~')
        self.__pencarian = kwargs.get('pencarian', '~')

    @property
    def pencarian(self):
        return self.__pencarian

    @pencarian.setter
    def pencarian(self, ):
        self.__pencarian = pencarian
