from sqlalchemy import Column, Integer, String
from dados.repositories.base import Base

class EstadoCivil(Base):
    __tablename__ = "estado_civil"

    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String(50), nullable=False, unique=True)
