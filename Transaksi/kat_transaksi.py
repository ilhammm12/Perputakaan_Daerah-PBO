from sqlachemy import create_engine, Column, Integer, String, Date, Boolean, ForeignKey
from sqlachemy.ext.declarative import declarative_base
from sqlachemy.orm import sessionmaker, relationship

class Peminjaman:
    def __init__(self, *args, **kwargs):
        self.__id_pinjam = kwargs.get('idpinjam','001')
        self.__id_agt = kwargs.get('idagt','001')
        self.__id_ptg = kwargs.get('idptg','001')
        self.__id_buku = kwargs.get('idbuku','001')
        self.__tanggalpinjam = kwargs.get('tanggalpinjam','20 January 2020')
        self.__tanggalkembali = kwargs.get('tanggalkembali','30 January 2020')

    @property
    def id_pinjam(self):
        return self.__id_pinjam
    @id_pinjam.setter
    def id_pinjam(self, value):
        self.__id_pinjam = value

    @property
    def id_agt(self):
        return self.__id_agt
    @id_agt.setter
    def id_agt(self, value):
        self.__id_agt = value

    @property
    def id_ptg(self):
        return self.__id_ptg
    @id_ptg.setter
    def id_ptg(self, value):
        self.__id_ptg = value

    @property
    def id_buku(self):
        return self.__id_buku
    @id_buku.setter
    def id_buku(self, value):
        self.__id_buku = value

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, value):
        self.__status = value

class pengembalian() :

    def __init__(self, *args, **kwargs):
        self.id_pengembalian = kwargs.get('id_pengembalian', 'K0001')
        self.denda = kwargs.get('denda', '25.000')

    @property
    def id_pengembalian(self):
        return self.id_pengembalian
    @id_pengembalian.setter
    def id_pengembalian(self, id_pengembalian):
        self.id_pengembalian = id_pengembalian

    @property
    def denda(self):
        return self.denda
    @denda.setter
    def denda(self, denda):
        self.denda = denda

class tb_transaksi(Base):
    __tablename__ = "tb_transaksi"

    id_pinjam = Column('id_pinjam', Integer, primary_key=True)
    id_anggota = Column('id_anggota', Integer, Unique=True)
    id_petugas = Column('id_petugas', Integer, Unique=True)
    id_buku = Column('id_buku', Integer, Unique=True)
    tgl_pinjam = Column('tgl_pinjam', Date)
    tgl_kembali = Column('tgl_kembali', Date)
    status = Column('status', Boolean)
    denda = Column('denda', Integer)

engine = create_engine('sqllite:///:memory:', echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
