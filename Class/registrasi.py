class registrasi():

    def __init__(self, *args, *kwargs):
        self.__no_regis = kwargs.get('no_regis', '0001')
        self.__nik = kwargs.get('nik', '1415089462')
        self.__nama = kwargs.get('nama', 'Wawan Ridwan') 
        self.__tempat_lahir = kwargs.get('tempat_lahir', 'Bandung') 
        self.__tgl_lahir = kwargs.get('tgl_lahir', '15/03/2000')
        self.__alamat = kwargds.get('alamat', 'Gg. Mulia') 
        self.__no_hp = kwargs.get('no_hp', '081247854462')
        self.__jenis_kelamin = kwargs.get('jenis_kelamin', 'laki-laki') 
        self.__jenis_anggota = kwargs.get('jenis_anggota', 'anggota') 

    @property
    def no_regis(self):
        return self.__no_regis
        
    @no_regis.setter
    def no_regis(self, no_regis):
        self.__no_regis = no_regis  
        
    @property
    def nik(self):
        return self.__nik
        
    @nik.setter
    def nik(self, nik):
        self.__nik = nik
        
    @property
    def nama(self):
        return self.__nama
        
    @nama.setter
    def nama(self, nama):
        self.__nama = nama
        
    @property
    def tempat_lahir(self):
        return self.__tempat_lahir
        
    @tempat_lahir.setter
    def tempat_lahir(self, tempat_lahir):
        self.__tempat_lahir = tempat_lahir
        
            
    @property
    def tgl_lahir(self):
        return self.__tgl_lahir
        
    @tgl_lahir.setter
    def tgl_lahir(self, tgl_lahir):
        self.__tgl_lahir = tgl_lahir
        
    @property
    def alamat(self):
        return self.__alamat
        
    @alamat.setter
    def alamat(self, alamat):
        self.__alamat = alamat
   
    @property
    def no_hp(self):
        return self.__no_hp
        
    @no_hp.setter
    def no_hp(self, no_hp):
        self.__no_hp = no_hp  
        
    @property
    def jenis_kelamin(self):
        return self.__jenis_kelamin
      
    @jenis_kelamin.setter
    def jenis_kelamin(self, jenis_kelamin):
        self.__jenis_kelamin = jenis_kelamin
        
    @property
    def jenis_anggota(self):
        return self.__jenis_anggota
       
    @jenis_anggota.setter
    def jenis_anggota(self, jenis_anggota):
        self.__jenis_anggota = jenis_anggota              	