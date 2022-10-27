from helpers.database import db


class Prefeitura(db.Model):

    def __init__(self, secretarios, email, telefone):
        self.secretarios = secretarios
        self.email = email
        self.telefone = telefone

    def __repr__(self):
        return '<Prefeitura %r>' % self.email
