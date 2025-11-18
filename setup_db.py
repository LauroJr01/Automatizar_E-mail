from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# 1. Cria a engine 
engine = create_engine("sqlite:///database.db", future=True) 

# 2. Cria sessão para conversar com o banco
Session = sessionmaker(bind=engine, future=True)
session = Session()

# ---------- BANCO DE DADOS ----------
Base = declarative_base()

class Motorista(Base):
    __tablename__ = "motoristas"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, unique=True, nullable=False)
    placa = Column(String, nullable=False)

class Email(Base):
    __tablename__ = 'emails'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)

Base.metadata.create_all(engine)
