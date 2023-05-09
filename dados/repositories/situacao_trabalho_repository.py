from sqlalchemy.orm import Session
from dados.models.situacao_trabalho import SituacaoTrabalho

class SituacaoTrabalhoRepository:

    def __init__(self, session: Session):
        self.session = session

    def get_all(self):
        return self.session.query(SituacaoTrabalho).all()

    def get_by_id(self, situacao_trabalho_id: int):
        return self.session.query(SituacaoTrabalho).filter(SituacaoTrabalho.id == situacao_trabalho_id).first()

    def create(self, descricao: str):
        situacao_trabalho = SituacaoTrabalho(descricao=descricao)
        self.session.add(situacao_trabalho)
        self.session.commit()
        return situacao_trabalho
