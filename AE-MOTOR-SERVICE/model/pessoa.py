
class Pessoa():

    def __init__(self, nome, dt_nascimento, email, telefone):
        self.nome = nome
        self.dt_nascimento = dt_nascimento
        self.email = email
        self.telefone = telefone

    def __repr__(self):
        return '<User %r>' % self.nome
