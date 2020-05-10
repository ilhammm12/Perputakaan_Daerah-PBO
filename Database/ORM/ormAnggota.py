from sqlachemy import create_engine, Column, Integer, String, Date, Boolean, ForeignKey
from Database.base import Base, sessionFactory

class ormAnggota(Base):
    __tablename__ = "tb_anggota"

    id_regis = Column('id_regis', Integer, primary_key=True)
    NIK = Column('NIK', Integer)
    Nama = Column('Nama', String)
    Tempat_lahir = Column('Tempat_lahir', String)
    Tanggal_lahir = Column('Tanggal_lahir', Date)
    Alamat = Column('Alamat', String)
    No_hp = Column('No_hp', Integer)
    Jenis_kelamin = Column('Jenis_kelamin', String)
