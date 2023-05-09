from sqlalchemy import Column, Integer, Date
from dados.repositories.base import Base
# from sqlalchemy.ext.declarative import declarative_base

# Base = declarative_base()

class Questionario(Base):
    __tablename__ = 'questionarios'

    id = Column(Integer, primary_key=True)
    domicilio_id = Column(Integer)
    recenseador_id = Column(Integer)
    data_coleta = Column(Date, nullable=False)
    idade = Column(Integer, nullable=False)
