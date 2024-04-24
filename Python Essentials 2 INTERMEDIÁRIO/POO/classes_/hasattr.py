# O Python fornece uma função capaz de verificar com segurança se algum objeto/classe contém uma propriedade 
# especificada. A função é chamada hasattr, e espera que lhe sejam transmitidos dois argumentos:

# A classe ou o objeto a ser verificado;
# o nome da propriedade cuja existência tem de ser comunicada (nota: tem de ser uma string contendo o nome do atributo, e não apenas o nome)
# A função devolve True ou False.

class Maioridade:
    def __init__(self, idade):
        if idade >= 18:
            self.dirigir = "sim"
        else:
            self.brincar = "sim"

# instanciando um objeto da classe Maioridade
pessoa = Maioridade(25)

if hasattr (pessoa, 'dirigir'):
    print("dirigir: ", pessoa.dirigir)
elif hasattr (pessoa, 'brincar'):
    print("Brincar: ", pessoa.brincar)


# a função hasattr() também pode operar em classes. Pode utilizá-la para descobrir 
# se uma variável de classe está disponível, tal como aqui no exemplo do editor.
# A função devolve True se a classe especificada contiver um determinado atributo, 
# e False caso contrário.

class teste:
    var1 = 1

# verificando existencia de atributos:
print("var1: ", hasattr(teste, 'var1'))   #True
print("var2: ", hasattr(teste, 'var2'))   #False
