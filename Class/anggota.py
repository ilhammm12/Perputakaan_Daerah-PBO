class Anggota:

    def __init__(self, *args, **kwargs):
        self.__id = kwargs.get('id','01')
        self.__nama = kwargs.get('nama','Baharudin')
        self.__alamat = kwargs.get('alamat','Karang Joang')
        self.__telpon = kwargs.get('telpon','085348992')
        self.__tempatlahir = kwargs.get('tempatlahir','Balikpapan')
        self.__tanggallahir = kwargs.get('tanggallahir','30 July 1995')
        self.__status = kwargs.get('status','anggota')

    def GetPencarian(self,):
        return

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def nama(self):
        return self.__nama
    @nama.setter
    def nama(self, value):
        self.__nama = value

    @property
    def alamat(self):
        return self.__alamat
    @alamat.setter
    def alamat(self, value):
        self.__alamat = value

    @property
    def telpon(self):
        return self.__telpon
    @telpon.setter
    def telpon(self, value):
        self.__telpon = value

    @property
    def tempatlahir(self):
        return self.__tempatlahir
    @tempatlahir.setter
    def tempatlahir(self, value):
        self.__tempatlahir = value

    @property
    def tanggallahir(self):
        return self.__tanggallahir
    @tanggallahir.setter
    def tanggallahir(self, value):
        self.__tanggallahir = value

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, value):
        self.__status = value
