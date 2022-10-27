from model.pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, prefeitura, cargo, nome, dt_nascimento, email, telefone):
        super().__init__(nome, dt_nascimento, email, telefone)
        self.prefeitura = prefeitura
        self.cargo = cargo