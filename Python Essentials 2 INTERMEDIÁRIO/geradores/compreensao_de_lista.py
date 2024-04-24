# A função list() pode transformar uma série de invocações de geradores subsequentes numa lista real:

lista = []

for element in range(10):
    lista.append(1 if element % 2 == 0 else 0)

print("lista: ", lista)

# compreensão de lista:
listaPares = ["par" if x % 2 == 0 else "impar" for x in range(10)]
print(listaPares)

# compreensão de listas vs geradores:
listaPares = ["par" if x % 2 == 0 else "impar" for x in range(10)]
gerador = ("par" if x % 2 == 0 else "impar" for x in range(10))

for x in listaPares:
    print(x, end=" ")
print()

for x in gerador:
    print(x, end=" ")
print()

# São os parêntesis. Os parêntesis retos fazem uma compreensão, os parêntesis curvos fazem um gerador.

# Como pode saber que a segunda tarefa cria um gerador, não uma lista?

# Há algumas provas que lhe podemos mostrar. Aplicar a função len() para ambas as entidades.

print(len(listaPares))  # output: 10
print(len(gerador))     # TypeError: object of type 'generator' has no len() 