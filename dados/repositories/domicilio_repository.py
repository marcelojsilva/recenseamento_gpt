from sqlalchemy.orm import Session
from dados.models.domicilio import Domicilio
from dados.models.recenseador import Recenseador
from dados.utils import is_foreign_key_valid

class DomicilioRepository:

    def __init__(self, session: Session):
        self.session = session

    def get_all(self):
        return self.session.query(Domicilio).all()

    def get_by_id(self, domicilio_id: int):
        return self.session.query(Domicilio).filter(Domicilio.id == domicilio_id).first()

    def create(self, tipo_residencia_id: int, endereco: str, numero: int, complemento: str, bairro: str, cidade: str, estado: str, cep: str, coordenadas: str, recenseador_id: int):
        if not is_foreign_key_valid(self.session, recenseador_id, Recenseador):
            raise ValueError("Recenseador não encontrado")

        domicilio = Domicilio(tipo_residencia_id=tipo_residencia_id, endereco=endereco, numero=numero, complemento=complemento, bairro=bairro, cidade=cidade, estado=estado, cep=cep, coordenadas=coordenadas, recenseador_id=recenseador_id)
        self.session.add(domicilio)
        self.session.commit()
        return domicilio