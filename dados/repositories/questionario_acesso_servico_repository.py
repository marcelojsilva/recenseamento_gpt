from sqlalchemy.orm import Session
from dados.models.questionario_acesso_servico import QuestionarioAcessoServico
from dados.models.questionario import Questionario
from dados.models.acesso_servico import AcessoServico
from dados.utils import is_foreign_key_valid

class QuestionarioAcessoServicoRepository:

    def __init__(self, session: Session):
        self.session = session

    def get_all(self):
        return self.session.query(QuestionarioAcessoServico).all()

    def get_by_id(self, questionario_acesso_servico_id: int):
        return self.session.query(QuestionarioAcessoServico).filter(QuestionarioAcessoServico.id == questionario_acesso_servico_id).first()

    def create(self, questionario_id: int, acesso_servico_id: int):
        if not is_foreign_key_valid(self.session, questionario_id, Questionario):
            raise ValueError("Questionário não encontrado")

        questionario_acesso_servico = QuestionarioAcessoServico(questionario_id=questionario_id, acesso_servico_id=acesso_servico_id)
        self.session.add(questionario_acesso_servico)
        self.session.commit()
        return questionario_acesso_servico
