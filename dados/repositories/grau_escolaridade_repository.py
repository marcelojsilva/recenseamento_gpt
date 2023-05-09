from sqlalchemy.orm import Session
from dados.models.grau_escolaridade import GrauEscolaridade

class GrauEscolaridadeRepository:

    def __init__(self, session: Session):
        self.session = session

    def get_all(self):
        return self.session.query(GrauEscolaridade).all()

    def get_by_id(self, grau_escolaridade_id: int):
        return self.session.query(GrauEscolaridade).filter(GrauEscolaridade.id == grau_escolaridade_id).first()

    def create(self, descricao: str):
        grau_escolaridade = GrauEscolaridade(descricao=descricao)
        self.session.add(grau_escolaridade)
        self.session.commit()
        return grau_escolaridade
