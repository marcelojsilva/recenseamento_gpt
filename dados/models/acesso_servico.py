from sqlalchemy import Column, Integer, String
from dados.repositories.base import Base

class AcessoServico(Base):
    __tablename__ = "acesso_servico"

    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String(100), nullable=False, unique=True)
