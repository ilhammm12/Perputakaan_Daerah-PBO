from sqlachemy import create_engine, Column, Integer, String, Date, Boolean, ForeignKey
from Database.base import Base, sessionFactory

Base = declarative_base()

class OrmPetugas(Base):

    __tablename__ = "tb_petugas"

    idPetugas = Column(Integer, primary_key=True)
    namaPetugas = Column('namaPetugas', String)
    tempatLahir = Column('tempatLahir', String)
    alamat = Column('alamat', String)
    email = Column('email', String)
    jenisKelamin = Column('jenisKelamin', String)
    idLaporan = Column('idLaporan', Integer, Unique=True)

