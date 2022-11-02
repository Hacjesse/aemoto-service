from model.aluno import Aluno
from helpers.database import db

class Passageiro(db.Model):

    __tablename__ = 'tb_passageiro'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(30), nullable=False)
    cidadeOrigem = db.Column(db.String(30), nullable=False)
    cidadeDestino = db.Column(db.String(30), nullable=False)
    
    def __init__(self, aluno, cidadeOrigem, cidadeDestino):
        self.aluno = aluno
        self.cidadeOrigem = cidadeOrigem
        self.cidadeDestino = cidadeDestino
    
    def __repr__(self):
        return '<Aluno {} Cidade Origem {} Cidade Destino {} >'.format(self.aluno, self.cidadeOrigem, self.cidadeDestino)
