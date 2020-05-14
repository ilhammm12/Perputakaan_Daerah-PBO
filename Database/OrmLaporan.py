from sqlachemy import create_engine, Column, Integer, String, Date, Boolean, ForeignKey
from Database.base import Base, sessionFactory

class OrmLaporan(base):
    __tablename__ = "laporan"

    id_laporan = Column('id_laporan', Integer, primary_key=True)
    jumlah_peminjaman = Column('jumlah_peminjaman', Integer, unique=True)
    bulan_tahun = Column('bulan_tahun', String)
    jumlah_pengunjung = Column('jumlah_pengunjung', Integer)
    
    def __init__(self, id_laporan,jumlah_peminjaman,bulan_tahun,jumlah_pengunjung):

        self.id_laporan = id_laporan
        self/jumlah_peminjaman = jumlah_peminjaman
        self.bulan_tahun = bulan_tahun
        self.jumlah_pengunjung = jumlah_pengunjung
        
Base.metadata.create_all(engine)
