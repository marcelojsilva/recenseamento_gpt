from sqlalchemy.orm import Session
from typing import List
from dados.models import Recenseador

class RecenseadorRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, recenseador: Recenseador) -> Recenseador:
        self.session.add(recenseador)
        self.session.commit()
        self.session.refresh(recenseador)
        return recenseador

    def get_by_id(self, id: int) -> Recenseador:
        return self.session.query(Recenseador).filter(Recenseador.id == id).first()

    def get_by_usuario(self, usuario: str) -> Recenseador:
        return self.session.query(Recenseador).filter(Recenseador.usuario == usuario).first()

    def get_all(self) -> List[Recenseador]:
        return self.session.query(Recenseador).all()
