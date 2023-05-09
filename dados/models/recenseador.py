from sqlalchemy import Column, Integer, String, Boolean, Date
from sqlalchemy.orm import relationship
from dados.repositories.base import Base

class Recenseador(Base):
    __tablename__ = "recenseadores"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    usuario = Column(String(50), nullable=False, unique=True)
    senha = Column(String(255), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    data_nascimento = Column(Date, nullable=False)
    ativo = Column(Boolean, nullable=False, default=True)

    domicilios = relationship("Domicilio", back_populates="recenseador")
