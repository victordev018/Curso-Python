'''
pedir ao utilizador para introduzir uma palavra;
usar user_word = user_word.upper() para converter a
palavra introduzida pelo utilizador em maiúsculas; 
falaremos sobre os chamados métodos de strings e o 
método upper() muito em breve - não se preocupe;
usar execução condicional e a declaração continue para 
“comer” as seguintes vogais A, E, I, O, U da palavra introduzida;
imprimir as letras não comidas para o ecrã, cada uma delas numa linha separada.
'''

word = input("word: ")
word = word.upper()

for letra in word:
    if letra in ["A", "E", "I", "O", "U"]:
        continue
    print(f"{letra}\n")