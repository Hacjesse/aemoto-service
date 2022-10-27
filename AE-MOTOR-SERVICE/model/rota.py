class Rota():
    def __init__(self, cidadeDestino, qtdAlunos, veiculo, passageiro, horarioSaida, horarioChegada, prefeitura):
        self.cidadeDestino = cidadeDestino
        self.qtdAlunos = qtdAlunos
        self.veiculo = veiculo
        self.passageiro = passageiro
        self.horarioSaida = horarioSaida
        self.horarioChegada = horarioChegada
        self.prefeitura = prefeitura

    def __repr__(self):
        return '<Cidade destino {}  Quantidade de Alunos  {} Veiculo {} Passageiro {} Hora de Saída {} Hora de chegada {} Prefeitura {}>'.format(self.cidadeDestino, self.qtdAlunos, self.veiculo, self.passageiro, self.horarioSaida, self.horarioChegada, self.prefeitura)

