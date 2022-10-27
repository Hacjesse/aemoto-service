from model.aluno import Aluno

class Passageiro(Aluno):
    def __init__(self, cidadeOrigem, cidadeDestino, instituicaoDeEnsino, curso, matricula, telefone):
        super().__init__(instituicaoDeEnsino, curso, matricula, telefone)
        self.cidadeOrigem = cidadeOrigem
        self.cidadeDestino = cidadeDestino
