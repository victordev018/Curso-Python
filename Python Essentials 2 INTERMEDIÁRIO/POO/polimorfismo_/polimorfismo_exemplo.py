# polimorfismo, é o poder das subclasses alterar o comportamento das superclasses:
class One:
    def mostre_na_tela(self):
        print("sou a primeira classe")

    def auxiliar(self):
        self.mostre_na_tela()

class Two(One):
    def mostre_na_tela(self):
        print("sou a segunda classe")

obj_one = One()
obj_two = Two() 

obj_one.auxiliar() #sou a primeira classe
obj_two.auxiliar() #sou a segunda classe

# comportamento de cada classe pode ser modificado em qualquer altura por qualquer uma das suas subclasses.