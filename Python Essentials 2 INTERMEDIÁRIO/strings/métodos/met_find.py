# A classe find() é semelhante a index(), que já conhece - procura uma substring e devolve o index 
# de primeira ocorrência desta substring, mas:

# é mais seguro - não gera um erro para um argumento que contém uma substring inexistente (devolve -1 então)
# funciona apenas com strings - não tente aplicá-lo a qualquer outra sequência.

nome = "Joaozinho"

print("\nposição 'z': ", nome.find('z')) #output: 4
print("posição 'l': ", nome.find('l')) #output: -1

# procurar uma substring a partir de um index específico:
# o sedundo argumento, especifica a partir de que index inicia-se a peesquisa
print("\nposição 'o': ", nome.find('o', 2)) #output: 3

# para procurar todas as posições que a substring aparece:
auxiliar = nome.find('o')
print("posições da letra 'o': ")
while auxiliar != -1: # enquanto, o index com a substring existir, ele repete
    print(auxiliar)
    auxiliar = nome.find('o', auxiliar + 1) # parte sem


# o método rfind(), tem executa a mesma função, porém, começa sua pesquisa do útimo elemento até o primeiro:
