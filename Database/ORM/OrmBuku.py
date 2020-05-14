from sqlalchemy import create_engine, Column, Integer, String, Date, Boolean, ForeignKey
from Database.base import Base, sessionFactory

class OrmBuku(base):
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

    @staticmethod
    def deleteBuku(buku):
        try:
            session = sessionFactory()
            session.query(buku).filter_by(id_buku=buku).delete()
            session.commit()
            session.close()
        except Exception as k:
            print("->", k)
        else:
            print("buku berhasih dihapus!!!")

    @staticmethod
    def getBuku(buku):
        try:
            id_bukuBaru= input("id buku Baru ")
            judul_bukuBaru = input("judul buku baru: ")
            Pengarang_bukuBaru = input("pengarang buku baru : ")
            Penerbit_bukuBaru = input("penerbit buku baru : ")
            thn_terbitbukuBaru = input("tahun terbit buku baru: ")
            stok_bukuBaru = input("stok buku baru: ")
            nmr_rakbukuBaru = input("nomor rak buku baru: ")
            session = sessionFactory()
            session.query(OrmBuku).filter_by(id_buku=buku).update({Bookorm.Booktype: newBooktpe, Bookorm.Bookname: newBookname, Bookorm.Author: newAuthor, Bookorm.Price: newPrice, BookormRackno: NewRackno, Bookormstatus: Newstatus}, synchronize_session=False)
            session.commit()
            session.close()
        except Exception as k:
            print("->", k)
        else:
            print("BERHASIL MENAMBAHKAN BUKU")




