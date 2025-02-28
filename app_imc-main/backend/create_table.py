from sqlalchemy import create_engine, Column, Integer, Float, Date, String
from sqlalchemy.orm import sessionmaker
import datetime


from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class ControlPesoAltura(Base):
    __tablename__ = 'control_peso_altura'
    id = Column(Integer, primary_key=True)
    fecha = Column(Date, nullable=False)
    peso_kg = Column(Float, nullable=False)
    altura_m = Column(Float, nullable=False)
    imc = Column(Float, nullable=False)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

def main():
    engine = create_engine('sqlite:///control_peso_altura.db', echo=True)
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    main()