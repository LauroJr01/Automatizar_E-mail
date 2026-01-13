from sqlalchemy import create_engine, Column, Integer, String, DECIMAL, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from datetime import datetime

# 1. Cria a engine 
engine = create_engine("sqlite:///database.db", future=True) 

# 2. Cria sessão para conversar com o banco
Session = sessionmaker(bind=engine, future=True)


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
    opcao_selecionada = Column(String, nullable=True)

class Dados(Base):
    __tablename__ = 'dados'
    id = Column(Integer, primary_key=True, autoincrement=True)
    motorista_id = Column(Integer, ForeignKey('motoristas.id'), nullable=False)
    local = Column(String, nullable=True)
    numero_carreta = Column(Integer, nullable=True)
    valor_frete = Column(DECIMAL(10,2), nullable=True)
    data = Column(String, default=datetime.now().strftime('%d/%m/%Y'))
    motorista = relationship("Motorista")
    
class EmailTemplate(Base):
    __tablename__ = 'email_templates'
    id = Column(Integer, primary_key=True, autoincrement=True)
    assunto = Column(String, nullable=False)
    corpo = Column(String, nullable=False)
    resposta_automatica = Column(String, nullable=True)

class EmailRegistro(Base):
    __tablename__ = 'emails_registro'

    id = Column(Integer, primary_key=True, autoincrement=True)

    # 🔑 Identidade Outlook
    entry_id = Column(String, nullable=False)
    store_id = Column(String, nullable=False)

    # 📬 Metadados
    assunto = Column(String, nullable=True)
    destinatario = Column(String, nullable=True)
    remetente = Column(String, nullable=True)

    # ⏱️ Datas
    data_criacao = Column(String,default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    data_envio = Column(String, nullable=True)
    data_recebimento = Column(String, nullable=True)

    # 🔄 Estado
    status = Column(String,default="recebido") # recebido | enviado | respondido | erro

    # 🔗 Negócio
    dados_id = Column(Integer, ForeignKey('dados.id'), nullable=True)
    dados = relationship("Dados")

Base.metadata.create_all(engine)
