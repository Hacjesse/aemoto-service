from model.pessoa import Pessoa
from helpers.database import db

class Prefeito(Pessoa, db.Model):
    def __init__(self, nome, dt_nascimento, email, telefone):
        super().__init__(nome, dt_nascimento, email, telefone)

    def __repr__(self):
        return '<Nome: {}\n Data de nascimento: {}\n Email: {}\n Telefone: {}>'.format(self.nome, self.dt_nascimento, self.email, self.telefone)
