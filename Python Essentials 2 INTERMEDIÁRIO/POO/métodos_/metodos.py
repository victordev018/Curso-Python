# criando classe aluno:
class Aluno:
    # todo método obrigatoriamente tem de ser croiado com um parâmetro
    # por conveção, usamos o self
    def InserirNotas(self, nota):
        pass

# O parâmetro self é utilizado para obter acesso à instância do objeto e às variáveis de classe.

# A função self é também utilizado para invocar outros métodos objeto/classe de dentro da classe.
class Classy:

    def other(self):
        print("other")

    def method(self):
        print("method")
        self.other()

obj = Classy()
obj.method()
