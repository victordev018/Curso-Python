# hotel: 3 edificios, cada um com 15 andares e 20 quartos em cada.

# tipo de arrzy: boolean.

hotel = [[[False for q in range(20)] for a in range(15)] for e in range(3)]  # q = quarto; a = andares; e = edificios

# Agora pode reservar um quarto para dois recém-casados: no segundo edifício, no décimo andar, quarto 14:
hotel [1] [9] [13] = True
print(hotel)