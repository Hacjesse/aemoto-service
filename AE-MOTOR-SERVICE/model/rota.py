from helpers.database import db

class Rota(db.Model):

    __tablename__ = "tb_rota"

    id = db.Column(db.Integer, primary_key=True)
    nomeDestino = db.Column(db.String(200), nullable=False)
    qtdalunos = db.Column(db.String(11), nullable=False)
    veiculo = db.Column(db.String(30), nullable=False)
    passageiro = db.Column(db.String(50), nullable=False)    
    horaSaida = db.Column(db.DateTime(), nullable=False)
    horaChegada = db.Column(db.DateTime(), nullable=False)
    prefeitura = db.Column(db.String(200), nullable=False)
    
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

