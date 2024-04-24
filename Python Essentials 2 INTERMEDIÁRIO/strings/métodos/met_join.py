# como o seu nome sugere, o método realiza uma junção (em inglês, join) - espera um argumento como uma lista;
# deve ter a certeza de que todos os elementos da lista são strings - o método irá levantar uma exceção TypeError 
# de outra forma;
# todos os elementos da lista serão unidos numa string, mas... a string a partir da qual o método foi invocado é 
# usada como um separador, colocado entre as strings; a string recém-criada é devolvida como um resultado.

#string contendo altura, o primeiro elemento representa a parte inteira em metros, o segundo a parte fracionária em centímetros:
print("altura: ", ",".join(['1', '72']))