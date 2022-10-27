from model.pessoa import Pessoa


class Aluno(Pessoa):
    def __init__(self, nome, dt_nascimento, email, telefone, instituicaoDeEnsino, curso, matricula):
        super().__init__(nome, dt_nascimento, email, telefone)
        self.instituicaoDeEnsino = instituicaoDeEnsino
        self.curso = curso
        self.matricula = matricula