# também é utilizável o slice em strings
# string[start:end:acada_quanto]; string[:] -> pega todos

nome = 'joaozinho'

print(nome[1:3])  # oa
print(nome[3:])   # aozinho
print(nome[:3])   # joa
print(nome[3:-2]) # aozi
print(nome[-3:7]) # n
print(nome[::2])  # jozno
print(nome[1::2]) # ooih