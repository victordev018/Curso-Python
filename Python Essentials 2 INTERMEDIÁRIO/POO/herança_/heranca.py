# o conceito de herança, consiste na habilidade de subclasses herdarem todos as
# entidades de sua superclasse, todos seus atributos, seus métodos e afins.

class Animais:  # superclasse
    pass

class Mamiferos(Animais): #subclasse da classe animais
    pass

class Gatinhos(Mamiferos): #subclasse de Mamiferos e também de animais
    pass

# issubclass(class1, class2), é capaz de ferificar a relação entre duas classes:
# se class1 for subclasse de class2, a função devolve True, outro caso, False.

print(issubclass(Gatinhos, Animais)) # True
print(issubclass(Mamiferos, Gatinhos)) # False

# a função isinstance(obj_name, class_name), verifica se um objeto for uma instância determinada classe
# devolve True, caso verdadeiro ou False, caso falso:

arnold = Gatinhos()
print(isinstance(arnold, Gatinhos)) #True
print(isinstance(arnold, Animais)) #True

# nota: arnold é uma instancia da classe animais mesmo tendo sido instanciado com a classe Gatinhos
# pois, gatinhos é uma subclasse de animais, todos seus objetos também são da classe Animais

# O operador is verifica se duas variáveis (object_one e object_two aqui) se referem ao mesmo objeto.
bolinha = Gatinhos()
gerard = bolinha
print(gerard is bolinha) #True