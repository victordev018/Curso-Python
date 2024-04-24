'''
Cenário
O comando break é utilizada para sair/terminar um loop.
Crie um programa que use um loop while e pede continuamente 
ao utilizador para introduzir uma palavra, a menos que o utilizador
introduza "chupacabra" como a palavra secreta de saída, caso em que 
a mensagem "You've successfully left the loop." deve ser impressa para 
o ecrã, e o loop deve terminar. Não imprima nenhuma das palavras introduzidas
pelo utilizador. Utilize o conceito de execução condicional e a break declaração.
'''


while True:
    word = input("word: ")
    if word == "chupacabra":
        print("You've successfully left the loop.")
        break
