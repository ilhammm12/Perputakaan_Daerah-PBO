from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///:memori', echo=True)
Base = declarative_base()

class bukuORM(base):
    __tablename__ = "Buku"

    id_buku = Column('id_buku', Integer, primary_key=True)
    judul_buku = Column('judul_buku', String, unique=True)
    pengarang = Column('pengarang', String)
    penerbit = Column('penerbit', String)
    tahun_terbit = Column('tahun_ternit', String)
    stok_buku = Column('stok_buku', String)
    nmr_rak = Column('nmr_rak', Integer)

    def __init__(self, id_buku, judul_buku, pengarang, penerbit, tahun_terbit, stok_buku, nomor_rak):

        self.id_buku = id_buku
        self.judul_buku = judul_buku
        self.pengarang = pengarang
        self.penerbit = penerbit
        self.tahun_terbit = tahun_terbit
        self.stok_buku = stok_buku
        self.nmr_rak = nomor_rak

Base.metadata.create_all(engine)
