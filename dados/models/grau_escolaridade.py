from sqlalchemy import Column, Integer, String
from dados.repositories.base import Base

class GrauEscolaridade(Base):
    __tablename__ = "grau_escolaridade"

    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String(100), nullable=False, unique=True)
