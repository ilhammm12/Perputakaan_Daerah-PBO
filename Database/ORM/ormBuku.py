from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///:memori', echo=True)
Base = declarative_base()

class bukuORM(base):
    __tablename__ = "buku"

    id_buku = colum('id_buku', integer, primary_key=True)
    judul_buku = colum('judul_buku', string, unique=True)
    pengarang = colum('pengarang', string)
    penerbit = colum('penerbit', string)
    tahun_terbit = colum('tahun_ternit', string)
    stok_buku = colum('stok_buku', string)
    nomor_rak = colum('nomor_rak', integer)

    def __init__(self, id_buku, judul_buku, pengarang, penerbit, tahun_terbit, stok_buku, nomor_rak):

        self.id_buku = id_buku
        self.judul_buku = judul_buku
        self.pengarang = pengarang
        self.penerbit = penerbit
        self.tahun_terbit = tahun_terbit
        self.stok_buku = stok_buku
        self.nomor_rak = nomor_rak

Base.metadata.create_all(engine)