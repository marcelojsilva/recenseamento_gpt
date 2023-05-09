from sqlalchemy.orm import Session
from dados.models.tipo_residencia import TipoResidencia

class TipoResidenciaRepository:

    def __init__(self, session: Session):
        self.session = session

    def get_all(self):
        return self.session.query(TipoResidencia).all()

    def get_by_id(self, tipo_residencia_id: int):
        return self.session.query(TipoResidencia).filter(TipoResidencia.id == tipo_residencia_id).first()

    def create(self, descricao: str):
        tipo_residencia = TipoResidencia(descricao=descricao)
        self.session.add(tipo_residencia)
        self.session.commit()
        return tipo_residencia
