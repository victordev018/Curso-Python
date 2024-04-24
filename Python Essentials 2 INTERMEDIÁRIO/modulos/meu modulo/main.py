import modulo

# crriando listas:
listaZeros = [0 for elements in range(5)]
listaOnes = [1 for elements in range(5)]

#  invocando os métodos do módulo
print("\nSoma lista 0: ", modulo.sumL(listaZeros))
print("Produto lista 1: ", modulo.prodL(listaOnes))

# usamos a entidade path, do módulo sys para localizar um módulo de outra pasta:
# from sys import path
# path.append('C:\\local\\local\\modulo')