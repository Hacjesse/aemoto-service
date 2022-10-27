class InstituicaoDeEnsino():
    def __init__(self, endereco, telefone, nome):
        self.endereco = endereco
        self.telefone = telefone
        self.nome = nome

    def __repr__(self):
        return '<Nome: {}\n Endereco: {}\n Telefone: {}>'.format(self.nome, self.endereco, self.telefone)