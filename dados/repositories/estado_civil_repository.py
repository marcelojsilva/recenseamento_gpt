from sqlalchemy.orm import Session
from dados.models.estado_civil import EstadoCivil

class EstadoCivilRepository:

    def __init__(self, session: Session):
        self.session = session

    def get_all(self):
        return self.session.query(EstadoCivil).all()

    def get_by_id(self, estado_civil_id: int):
        return self.session.query(EstadoCivil).filter(EstadoCivil.id == estado_civil_id).first()

    def create(self, descricao: str):
        estado_civil = EstadoCivil(descricao=descricao)
        self.session.add(estado_civil)
        self.session.commit()
        return estado_civil
