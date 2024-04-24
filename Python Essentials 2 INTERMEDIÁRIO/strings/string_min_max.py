# função min() com strings:

print(min("fdsAkB")) #output: 'A', devido as letras ocuparem os primeiros locais ntablela ASCII

# Neste caso, o espaço será a min prioridade
frase = 'O Jota é um ótimo dev'
print('[' + min(frase) + ']') #output: [ ]

# nest caso o min() prioridade seria o 0
numberes = [9, 8, 0]
print(min(numberes))  #output: 0

# da mesmma forma podemos usar a função max(), para encontrar o valor max da string
print(max("fdsAkB")) #output: 's', devido as letras ocuparem os primeiros locais ntablela ASCII

# Neste caso, o espaço será a max prioridade
frase = 'O Jota é um ótimo dev'
print('[' + max(frase) + ']') #output: [ó]

# nest caso o max() prioridade seria o 0
numberes = [9, 8, 0]
print(max(numberes))  #output: 9