# identificar palindromos(frase ou palavras que qunaod lidas de trás pra frente, possuem o mesmo significado).
texto = input("Enter a text: ")
vetorTexto = texto.split()
vetor2 = []
vetor2.append(vetorTexto.reverse())

print("vetor normal: ", vetorTexto)
print("vetor inverse: ", vetor2)

# if vectorTextInverse == vetorTexto:
#     print("IS a palindromos")