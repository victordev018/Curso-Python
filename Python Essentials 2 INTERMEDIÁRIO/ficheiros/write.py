# O método é chamado write() e espera apenas um argumento - uma string que será transferida para um 
# ficheiro aberto (não esquecer - o modo aberto deve refletir a forma como os dados são transferidos
# escrever um ficheiro aberto em modo de leitura não será bem sucedido).

stream = open("arquivoteste.txt", "wt")

for palavra in range(5):
    word = f"#{palavra} jota\n"
    for letra in word:
        stream.write(letra)
stream.close()

# Os loops open() devolve um objeto iterável que pode ser utilizado para iterar através de todas as linhas 
# do ficheiro dentro de um loop for . Por exemplo:

# for line in open("file", "rt"):
#     print(line, end='')


# O código copia o conteúdo do ficheiro para a consola, linha a linha. Nota: o stream fecha-se automaticamente 
# quando chega ao fim do ficheiro.

for linha in open("arquivoteste.txt", "rt"):
    print(linha, end='')