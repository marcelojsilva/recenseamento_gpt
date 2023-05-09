from sqlalchemy import Column, Integer, String
from dados.repositories.base import Base

class TipoResidencia(Base):
    __tablename__ = "tipo_residencia"

    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String(100), nullable=False, unique=True)
