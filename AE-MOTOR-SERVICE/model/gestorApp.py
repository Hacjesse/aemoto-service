from model.pessoa import Pessoa

class GestorApp(Pessoa):
    def __init__(self, nome, dt_nascimento, email, telefone):
        super().__init__(nome, dt_nascimento, email, telefone)
