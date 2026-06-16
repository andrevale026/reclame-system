from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

from config import DATABASE_URL

Base = declarative_base()

class Denuncia(Base):
    __tablename__ = "denuncias"

    id = Column(Integer, primary_key=True)

    # Dados gerais
    protocolo = Column(String(100), unique=True)
    tipo = Column(String(100))
    categoria_ia = Column(String(100))
    prioridade = Column(String(50))

    # Identificação
    email = Column(String(255))

    # Assédio
    assediado = Column(String(255))
    assediador = Column(String(255))
    ocupacao = Column(String(100))
    local_ocorrencia = Column(String(255))
    data_ocorrencia = Column(String(50))
    hora_ocorrencia = Column(String(50))

    # Aluno
    curso = Column(String(255))
    aluno_denunciado = Column(String(255))

    # Professor
    nome_professor = Column(String(255))
    disciplina = Column(String(255))

    # Técnico
    nome_tecnico = Column(String(255))

    # Infraestrutura
    area_infraestrutura = Column(String(255))

    # Relato principal
    relato = Column(Text)

    # LGPD
    dados_criptografados = Column(Text)

    # Auditoria
    criado_em = Column(DateTime, default=datetime.utcnow)

engine = create_engine(DATABASE_URL)

Base.metadata.create_all(engine)

print("Tabela denuncias criada com sucesso!")