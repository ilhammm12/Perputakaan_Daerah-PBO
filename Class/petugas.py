class petugas():

    def __init__(self, *args, **kwargs):
        self.__id_petugas = kwargs.get('id_petugas', '456')
        self.__nama_petugas = kwargs.get('nama_petugas', 'Dwianti')
        self.__tempat_lahir = kwargs.get('tempat_lahir', 'Samarinda, 14 maret 2000')
        self.__alamat = kwargs.get('alamat', 'Muara Badak')
        self.__email = kwargs.get('email', 'dwianti@gmail.com')
        self.__jenis_kelamin = kwargs.get('jenis_kelamin', 'perempuan')
        
        @property
        def id_petugas(self):
            return self.__id_petugas

        @id_petugas.setter
        def id_petugas(self, id_petugas):
            self.__id_petugas = id_petugas

        @property
        def nama_petugas(self):
            return self.__nama_petugas

        @nama_petugas.setter
        def nama_petugas(self, nama_petugas):
            self.__nama_petugas = nama_petugas

        @property
        def tempat_lahir(self):
            return  self.__tempat_lahir

        @tempat_lahir.setter
        def tempat_lahir(self, tempat_lahir):
            self.__tempat_lahir = tempat_lahir

        @property
        def alamat(self) :
            return  self.__alamat

        @alamat.setter
        def alamat(self, alamat):
            self.__alamat = alamat

        @property
        def email(self):
            return self.__email

        @email.setter
        def email(self, email):
            self.__email = email

        @property
        def jenis_kelamin(self):
            return self.__jenis_kelamin

        @jenis_kelamin.setter
        def jenis_kelamin(self, jenis_kelamin):
            self.__jenis_kelamin = jenis_kelamin
