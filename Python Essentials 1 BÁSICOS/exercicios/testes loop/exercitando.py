# for i in range(10): # apenas 1 parâmentro
#     print("The value of i is currently", i) #espera-se que imprima os valores de 0 ate 9

# for i in range(2, 8): # Dois parâmetros
#     print("The value of i is currently", i) #espera-se que imprima os valores começando do 2 até  o 7

# for i in range(2, 8, 3): # Três parâmetros
#     print("The value of i is currently", i) #o terceiro parâmetro indica o incremento a cada loop, nesse caso será impresso do 2 até o 5
# for i in range(1, 1):
#     print("The value of i is currently", i) # nesse caso nada será impresso, o intervalo começa no 1 e termina no mesmo, logo ele não pode ser exibido.

power = 1
for expo in range(16):
    print("2 to the power of", expo, "is", power)
    power *= 2