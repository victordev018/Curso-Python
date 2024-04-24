from datetime import time
# para criar um objeto com o tempo, o módulo datatime possue uma classe chamada time
horaQualquer = time(13,24,36) # hours, minutes and seconds

print("Hora: ", horaQualquer)

# o método sleep(), suspende a execução do programa durante um determinado número de segundos.
import time
print("hello...")
time.sleep(3)
print("World!")

# para pegar a hora atual, podemos usar o método ctime:
horaAtual = time.ctime()
print("Hora atual: ", horaAtual)

# No módulo datetime , data e hora podem ser representados como objetos separados ou como um só. 
# A classe que combina data e hora é chamada datetime.
from datetime import datetime
dt = datetime(2023, 4, 23, 15, 51, 33) # datatime(), data e hora:
print("Datatime: ", dt)
print("Date: ", dt.date())
print("Time: ", dt.time())

# métodos que devolvem data e hora atual:
# today(), now() e utcnow()
print("today: ", datetime.today())
print("now: ", datetime.now())

# A função timestamp devolve um valor float expressando o número de segundos decorridos entre 
# a data e a hora indicada pelo objeto datetime e 1 de janeiro de 1970, 00:00:00 (UTC).

from datetime import datetime
diaD = datetime(2021,2,5,21,36)

print("Timestamp: ", diaD.timestamp()) # retorna tempo em segundos