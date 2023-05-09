from sqlalchemy import Column, Integer, String
from dados.repositories.base import Base

class Parentesco(Base):
    __tablename__ = "parentescos"

    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String(50), nullable=False, unique=True)
