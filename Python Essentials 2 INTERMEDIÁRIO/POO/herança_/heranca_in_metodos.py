# como funciona a herança em métodos:

class Main:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f'My name is {self.name}.'
    
# subclasse de Main:
class Sub(Main):
    def __init__(self, name):
        Main.__init__(self, name) # no lugar de "Main", podemos usar a função super(), ele acede a 
pass                                 # super classe sem a necessidade de saber seu nome

# instanciando objeto da classe Sub:
pessoa1 = Sub("João")
print(pessoa1)