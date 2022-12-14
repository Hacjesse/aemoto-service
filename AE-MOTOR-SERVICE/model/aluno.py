from model.pessoa import Pessoa
from helpers.database import db

class Aluno(Pessoa, db.Model):

    id = db.Column(db.Integer, primary_key=True)
    instituicaoDeEnsino = db.Column(db.String(80), nullable=False)
    curso = db.Column(db.String(50), nullable=False)
    matricula = db.Column(db.String(20), nullable=False)

    parent_id = db.Column(db.Integer, db.ForeignKey("tb_pessoa.id"))
    parent = db.relationship("Pessoa")

    def __init__(self, nome, dt_nascimento, email, telefone, instituicaoDeEnsino, curso, matricula):
        super().__init__(nome, dt_nascimento, email, telefone)
        self.instituicaoDeEnsino = instituicaoDeEnsino
        self.curso = curso
        self.matricula = matricula

    def __repr__(self):
        return '<Nome: {}\n Nascimento: {}\n Email: {}\n Telefone: {}\n Instituição de ensino: {}\n Curso: {}\n Matrícula: {}>'.format(self.nome, self.dt_nascimento, self.email, self.telefone, self.instituicaoDeEnsino, self.curso, self.matricula)
