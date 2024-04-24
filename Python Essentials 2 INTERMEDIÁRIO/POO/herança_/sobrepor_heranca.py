# sobrepondo valores na herança:
class level1:
    var = 1
    def fun(self):
        return 2

class level2(level1):
    var = 2
    def fun(self):
        return 3
    
class level3(level2):
    pass

objeto = level3()

#quando o objeto for acessar os valores de var e fun, será exibido o da classe level2
#pois como tem o mesmo nome da classe level1, irá sobrepor os valores, será exibido
#o da útima alteração
print(objeto.var, objeto.fun())  # 2 3
