# o método endswith(), devolve True quando a string termina com o ragumento passado, outro caso, False:
nome = "João"

if nome.endswith("ão"):
    print(f"Sim, {nome} termina com ão")
else:
    print(f"Não, {nome} termina com ão")

# a classe startswith(), verifica se uma string, começa com a substring especificada:
print(nome.startswith('Jo'))  # True