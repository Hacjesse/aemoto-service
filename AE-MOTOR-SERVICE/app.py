from model.aluno import Aluno
from model.cidade import Cidade
from model.endereco import Endereco
from model.funcionario import Funcionario
from model.gestorApp import GestorApp
from model.instituicaoDeEnsino import InstituicaoDeEnsino
from model.motorista import Motorista
from model.passageiro import Passageiro
from model.pessoa import Pessoa
from model.prefeito import Prefeito
from model.prefeitura import Prefeitura
from model.rota import Rota
from model.uf import Uf
from model.veiculo import Veiculo


aluno = Aluno("Joao", "10/06/1998", "email@example.com", "9998-9876", "IFPB", "TSI", "202043210004")
print(aluno)

endereco = Endereco("58244-000", "345", "apartamento", "perto do canto ali", "Rua joao pessoa")
print(endereco)

funcionario = Funcionario("prefeitura", "Assistente")
print(funcionario)

gestorApp = GestorApp("Michael", "15/11/2000", "michael@example.com", "98875543")
print(gestorApp)

instituicaoDeEnsino = InstituicaoDeEnsino("Rua fulano", "91345564", "IFCG")
print(instituicaoDeEnsino)

motorista = Motorista("br-21", "Guarabira")
print(motorista)

pessoa = Pessoa("pedro", "15/06/2004", "email@example.com", "45765-7892")
print(pessoa)

gestor = GestorApp("Marcelo", "10/05/1998", "Mah@example.com", "99987456")
print(gestor)

