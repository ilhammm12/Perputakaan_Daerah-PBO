from sqlachemy import create_engine, Column, Integer, String, Date, Boolean, ForeignKey
from Database.base import Base, sessionFactory

class OrmRegistrasi(base):
    __tablename__ = "registrasi"

    no_regis = Column('no_regis', Integer, primary_key=True)
    nik = Column('nik', Integer, unique=True)
    nama = Column('nama', String)
    tempat_lahir = Column('tempat_lahir', String)
    tgl_lahir = Column('tgl_lahir', Date)
    alamat = Column('alamat', String)
    no_hp = Column('no_hp', Integer)
    jenis_kelammin = Column('jenis_kelamin', String)
    jenis_anggota = Column('jenis_anggota', String)

    def __init__(self, no_regis,nik,nama,tempat_lahir,tgl_lahir,alamat,no_hp,jenis_kelamin,jenis_anggota):

        self.no_regis = no_regis
        self.nik = nik
        self.nama = nama
        self.tempat_lahir = tempat_lahir
        self.tgl_lahir = tgl_lahir
        self.alamat = alamat
        self.no_hp = no_hp
        self.jenis_kelammin = jenis_kelamin
        self.jenis_anggota = jenis_anggota

Base.metadata.create_all(engine)
