from sqlalchemy import Column, Integer, String
from dados.repositories.base import Base  # esta linha substitui as duas linhas comentadas abaixo
# from sqlalchemy.ext.declarative import declarative_base

# Base = declarative_base()

class Domicilio(Base):
    __tablename__ = 'domicilios'

    id = Column(Integer, primary_key=True)
    endereco = Column(String(255), nullable=False)
    numero = Column(String(10), nullable=False)
    complemento = Column(String(100))
    bairro = Column(String(100), nullable=False)
    cidade = Column(String(100), nullable=False)
    estado = Column(String(2), nullable=False)
    recenseador_id = Column(Integer)
