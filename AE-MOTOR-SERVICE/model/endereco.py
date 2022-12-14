from helpers.database import db

class Endereco(db.Model):

    __tablename__ = "tb_endereco"

    id = db.Column(db.Integer, primary_key=True)
    cep = db.Column(db.String(10), nullable=False)
    numero = db.Column(db.String(6), nullable=False)
    complemento = db.Column(db.String(30), nullable=False)
    referencia = db.Column(db.String(300), nullable=False)
    logradouro = db.Column(db.String(100), nullable=False)

    def __init__(self, cep, numero, complemento, referencia, logradouro):
        self.cep = cep
        self.numero = numero
        self.complemento = complemento
        self.referencia = referencia
        self.logradouro = logradouro

    def __repr__(self):
        return '<CEP: {}\n Numero: {}\n Complemento: {}\n Referencia: {}\n Logradouro: {}>'.format(self.cep, self.numero, self.complemento, self.referencia, self.logradouro)
