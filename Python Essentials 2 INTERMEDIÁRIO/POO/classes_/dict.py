# __dict__, cria um sicionário com todas as propriedades atuais de um objeto
class Pessoa:
    def __init__(self, nome, idade):
        self.__nomes = []
        self.__idades = []
        self.__nomes.append(nome)
        self.__idades.append(idade)


#instanciando um objeto pessoa:
jota = Pessoa("joazinho", 18)

#__dict__ mostra as propriedades de um objeto de uma determinada classe, em forma de dicionário
print(jota.__dict__)