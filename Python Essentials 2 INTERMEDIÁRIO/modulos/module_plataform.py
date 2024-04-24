# A função platform permite-lhe aceder aos dados da plataforma subjacente, ou seja, 
# hardware, sistema operativo, e informação da versão do intérprete.

from platform import platform

# como invoc-la
# platform(aliased=False, terse=False)

# invocando a o plataform, para saber informações sobre a maquina
print(platform())
print(platform(1))
print(platform(0, 1))

# verificando se o sistema é o windows:
if "Windows" in platform(0,1):
    print("estamos no windows")

# machine(), serve para ver o nome genérico processador:
from platform import machine
print("Nome genérico Processador: ", machine())

# A função processor() devolve uma string preenchida com o nome do processador real (se possível).
from platform import processor
print("Nome processador: ", processor())

# Uma função chamada system() devolve o nome genérico do SO como uma cadeia.
from platform import system
print("Sistema operacional: ", system())

# A função version(), fornece a versão do SO
from platform import version
print("Versão do SO: ", version())
