from sqlachemy import create_engine, Column, Integer, String, Date, Boolean, ForeignKey
from sqlachemy.ext.declarative import declarative_base
from sqlachemy.orm import sessionmaker, relationship

class ormTransaksi(Base):
    __tablename__ = "tb_transaksi"

    id_pinjam = Column('id_pinjam', Integer, primary_key=True)
    id_anggota = Column('id_anggota', Integer, Unique=True)
    id_petugas = Column('id_petugas', Integer, Unique=True)
    id_buku = Column('id_buku', Integer, Unique=True)
    tgl_pinjam = Column('tgl_pinjam', Date)
    tgl_kembali = Column('tgl_kembali', Date)
    status = Column('status', Boolean)
    denda = Column('denda', Integer)
