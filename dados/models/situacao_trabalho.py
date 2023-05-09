from sqlalchemy import Column, Integer, String
from dados.repositories.base import Base

class SituacaoTrabalho(Base):
    __tablename__ = "situacao_trabalho"

    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String(100), nullable=False, unique=True)
