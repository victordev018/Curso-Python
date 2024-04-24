# para formatar a data da maneira como quiser, podemos usar o método strftime():
from datetime import date

data_atual = date.today() # fornece a data arual
print("date: ", data_atual)  # não formatada
print("date: ", data_atual.strftime("%d/%m/%y")) # data formatada

# para o time funciona da mesma maneira:
from datetime import time
hora_qualquer = time(16, 32)
print("Hora atual: ", hora_qualquer.strftime("%H:%M:%S"))
