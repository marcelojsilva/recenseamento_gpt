from sqlalchemy.orm import Session
from dados.models.parentesco import Parentesco

class ParentescoRepository:

    def __init__(self, session: Session):
        self.session = session

    def get_all(self):
        return self.session.query(Parentesco).all()

    def get_by_id(self, parentesco_id: int):
        return self.session.query(Parentesco).filter(Parentesco.id == parentesco_id).first()

    def create(self, descricao: str):
        parentesco = Parentesco(descricao=descricao)
        self.session.add(parentesco)
        self.session.commit()
        return parentesco
