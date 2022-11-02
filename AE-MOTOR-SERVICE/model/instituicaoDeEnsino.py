from helpers.database import db

class InstituicaoDeEnsino(db.Model):

    __tablename__ = "tb_instituicaoDeEnsino"

    id = db.Column(db.Integer, primary_key=True)
    endereco = db.Column(db.String(50), nullable=False)
    telefone = db.Column(db.String(13), nullable=False)
    nome = db.Column(db.String(20), nullable=False)

    def __init__(self, endereco, telefone, nome):
        self.endereco = endereco
        self.telefone = telefone
        self.nome = nome

    def __repr__(self):
        return '<Nome: {}\n Endereco: {}\n Telefone: {}>'.format(self.nome, self.endereco, self.telefone)