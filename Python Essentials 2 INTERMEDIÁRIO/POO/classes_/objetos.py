# Classe alunos:
class Aluno:
    def __init__(self):
        self.nome = ""
        self.idade = 0
        self.nota1 = 0
        self.nota2 = 0

    def Media(self, nota1, nota2):
        soma = nota1 + nota2
        return soma/2

# qunatidade de alunos a serem cadastrados:       
quantidade_alunos = int(input("> quantidade de alunos: "))

#listas de dados:
Nomes = []
Idades = []
Medias = []

# inserção de dados/informação de cada aluno:
for aluno in range(quantidade_alunos):
    print(f"\n{aluno+1}° aluno:")
    novoAluno = Aluno()
    novoAluno.nome = input("> nome: ")
    novoAluno.idade = int(input("> idade: "))
    novoAluno.nota1 = float(input("> nota1: "))
    novoAluno.nota2 = float(input("> nota2: "))

    # armazenando nas liastas:
    Nomes.append(novoAluno.nome)
    Idades.append(novoAluno.idade)
    Medias.append(novoAluno.Media(novoAluno.nota1, novoAluno.nota2))

print("")
for aluno in range(len(Nomes)):
    print(Nomes[aluno], " idade :", Idades[aluno], " media:", Medias[aluno])

# print("Idade pedro: ", aluno1.idade)
# print("Idade felipe: ", aluno2.idade)
# print("media Pedro: ", aluno1.Media(aluno1.nota1, aluno1.nota2))
# print("media Felipe: ", round(aluno2.Media(aluno2.nota1, aluno2.nota2)))