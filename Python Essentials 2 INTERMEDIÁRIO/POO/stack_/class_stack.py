# criando uma classe Stack:
class Stack:
    # será invocado na criação de um novo obj, implicitamente
    def __init__(self):  # construtor
        # vamos encapsular nossa stack_lista.
        self.__stack_list = []

    #método push:
    def push(self, value):
        self.__stack_list.append(value)

    #método pop:
    def pop(self):
        value = self.__stack_list[-1]
        del self.__stack_list[-1]
        return value


# instanciando um objeto
stack_obeto = Stack()
# print(len(stack_obeto.___stack_list)) # causará erro, pois a entidade é prrivada

# nota: Quando qualquer componente de classe tem um nome que começa com 
# dois underscores (__), torna-se privado 

# adiicionando valores no stack
stack_obeto.push(3)
stack_obeto.push(2)
stack_obeto.push(1)

# tirando elementos do stack
print(stack_obeto.pop())  #1
print(stack_obeto.pop())  #2
print(stack_obeto.pop())  #3


# Todos os métodos têm de ter este parâmetro(self). Desempenha o mesmo papel que o primeiro parâmetro construtor.
# Permite ao método aceder a entidades (propriedades e atividades/métodos) realizadas pelo objeto atual. 

# podemos criar um novo objeto da classe Stack, criará uma __stack_list específica para o objeto instanciado:
stack_obeto_1 = Stack()
stack_obeto_2 = Stack()

stack_obeto_1.push(3)
stack_obeto_2.push(stack_obeto_1.pop())

print("\nstack object 2: ",stack_obeto_2.pop())

# Existem duas stacks criadas a partir da mesma classe base. Elas trabalham de forma independente.
# Pode fazer mais delas se o desejar.

# criando uma subclasse de Stack, a nova classe deve ser capaz de avaliar a soma de todos os 
# elementos atualmente armazenados na stack.]
 

# invocar um método de dentro da classe exige o uso explícito do argumento self , 
# e tem de ser colocado em primeiro lugar na lista.
class SomarStack(Stack):    #subclass de Stack
    def __init__(self):
        Stack.__init__(self)
        self.__soma = 0
    # para obter o valor de soma dos elementos da pilha
    def get_soma(self):
        return self.__soma

    def push(self, value):
        self.__soma += value
        Stack.push(self, value)
    
    def pop(self):
        val = Stack.pop
        self.__soma -= 1
        return val
    
meu_objeto = SomarStack()

#adicionando 5 valores:
for value in range(5):
    meu_objeto.push(value)
print("Soma: ", meu_objeto.get_soma()) #output 10