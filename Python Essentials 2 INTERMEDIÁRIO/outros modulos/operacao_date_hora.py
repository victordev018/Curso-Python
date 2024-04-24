# Para criar um objeto timedelta , basta fazer a subtração nos objetos date ou datetime , 
# assim como fizemos no exemplo no editor. Execute-o.

from datetime import date
from datetime import datetime

d1 = date(2020, 11, 4)
d2 = date(2019, 11, 4)

print(d1 - d2)  #timedelta

dt1 = datetime(2020, 11, 4, 0, 0, 0)
dt2 = datetime(2019, 11, 4, 14, 53, 0)

print(dt1 - dt2)

# criando um timedelta:
from datetime import timedelta
delta = timedelta(days=8, weeks=2, hours=5, minutes=59, seconds=59)
print("Timedelta: ", delta)  # retorna o tempo em dias, horas, minutos e secgundos

# mais operações com timedelta:
print("\nOperações timedelta: ")
delta = timedelta(weeks=2, days=2, hours=2)
print(delta) # 16 days, 2:00:00

delta2 = delta * 2
print(delta2)# 32 days, 4:00:00

d = date(2019, 10, 4) + delta2
print(d) # 2019-11-05

dt = datetime(2019, 10, 4, 14, 53) + delta2
print(dt) #1019-11-05 18:53:00