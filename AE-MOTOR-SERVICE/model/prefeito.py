from model.pessoa import Pessoa


class Prefeito(Pessoa):
    def __init__(self, nome, nascimento, email, telefone):
        super().__init__(nome, nascimento, email, telefone)
