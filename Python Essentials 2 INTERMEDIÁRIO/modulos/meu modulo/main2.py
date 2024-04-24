# Vamos aceder à função funI() do módulo iota a partir do topo do pacote extra .

# importando o path(), para poder localizar o pacote "extra"
from sys import path

path.append('C:\JV past\Labiras\curso python\Python Essentials 2 INTERMEDIÁRIO')

# importar iota
from extra.iota import FunI
print(FunI())

# importando sigma e tal
import extra.good.best.sigma as sig
from extra.good.best.tau import FunT as alp

print(sig.FunS())
print(alp())
