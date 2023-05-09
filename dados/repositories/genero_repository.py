from sqlalchemy.orm import Session
from dados.models.genero import Genero

class GeneroRepository:

    def __init__(self, session: Session):
        self.session = session

    def get_all(self):
        return self.session.query(Genero).all()

    def get_by_id(self, genero_id: int):
        return self.session.query(Genero).filter(Genero.id == genero_id).first()

    def create(self, descricao: str):
        genero = Genero(descricao=descricao)
        self.session.add(genero)
        self.session.commit()
        return genero
