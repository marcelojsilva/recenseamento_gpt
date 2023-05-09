from sqlalchemy.orm import Session
from dados.models.acesso_servico import AcessoServico

class AcessoServicoRepository:

    def __init__(self, session: Session):
        self.session = session

    def get_all(self):
        return self.session.query(AcessoServico).all()

    def get_by_id(self, acesso_servico_id: int):
        return self.session.query(AcessoServico).filter(AcessoServico.id == acesso_servico_id).first()

    def create(self, descricao: str):
        acesso_servico = AcessoServico(descricao=descricao)
        self.session.add(acesso_servico)
        self.session.commit()
        return acesso_servico
