from model.funcionario import Funcionario

class Motorista(Funcionario):
    def __init__(self, rotas, prefeitura, cargo, nome, dt_nascimento, email, telefone):
        super().__init__(prefeitura, cargo, nome, dt_nascimento, email, telefone)
        self.rotas = rotas

    def __repr__(self):
        return '<Rotas {}\n Prefeitura {}\n Cargo {}>'.format(self.rotas, self.prefeitura, self.cargo)