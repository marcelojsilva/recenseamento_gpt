from sqlalchemy.orm import Session
from dados.models.questionario import Questionario
from dados.models.domicilio import Domicilio
from dados.models.recenseador import Recenseador
from dados.utils import is_foreign_key_valid

class QuestionarioRepository:

    def __init__(self, session: Session):
        self.session = session

    def get_all(self):
        return self.session.query(Questionario).all()

    def get_by_id(self, questionario_id: int):
        return self.session.query(Questionario).filter(Questionario.id == questionario_id).first()

    def create(self, domicilio_id: int, recenseador_id: int, data_coleta: str, idade: int):
        if not is_foreign_key_valid(self.session, domicilio_id, Domicilio):
            raise ValueError("Domicilio não encontrado")

        if not is_foreign_key_valid(self.session, recenseador_id, Recenseador):
            raise ValueError("Recenseador não encontrado")

        questionario = Questionario(domicilio_id=domicilio_id, recenseador_id=recenseador_id, data_coleta=data_coleta, idade=idade)
        self.session.add(questionario)
        self.session.commit()
        return questionario

