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
