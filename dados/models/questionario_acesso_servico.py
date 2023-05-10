from sqlalchemy import Column, Integer
from dados.repositories.base import Base

class QuestionarioAcessoServico(Base):
    __tablename__ = 'questionario_acesso_servico'

    id = Column(Integer, primary_key=True)
    questionario_id = Column(Integer)
    acesso_servico_id = Column(Integer)
