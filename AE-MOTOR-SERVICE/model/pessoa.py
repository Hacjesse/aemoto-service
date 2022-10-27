
class Pessoa():

    def __init__(self, nome, dt_nascimento, email, telefone):
        self.nome = nome
        self.dt_nascimento = dt_nascimento
        self.email = email
        self.telefone = telefone

    def __repr__(self):
        return '<Nome: {}\n Data de Nascimento: {}\n Email: {}\n Telefone: {}>'.format(self.nome, self.dt_nascimento, self.email, self.telefone)
