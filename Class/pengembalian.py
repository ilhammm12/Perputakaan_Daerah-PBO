class pengembalian() :

    def __init__(self, *args, **kwargs):
        self.id_pengembalian = kwargs.get('id_pengembalian', 'K0001')
        self.denda = kwargs.get('denda', '25.000')

    @property
    def id_pengembalian(self):
        return self.id_pengembalian
    @id_pengembalian.setter
    def id_pengembalian(self, id_pengembalian):
        self.id_pengembalian = id

    @property
    def denda(self):
        return self.denda
    @denda.setter
    def denda(self, denda):
        self.denda = denda
        
