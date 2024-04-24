def main():
    professores = "Rogério,Ricardo,Ezequias,Lilian,,"
    listaProfessores = mySplit(professores)
    print(listaProfessores)

def mySplit(_str, sep=" "):
    lista = []
    aux = ""
    for i in range(len(_str)):
        letraAtual = _str[i]
        if letraAtual == sep:
            lista.append(aux)
            aux = ""
        elif i == len(_str) - 1: # caso seja a ultima letra
            aux += letraAtual
            lista.append(aux)
        else:
            aux += letraAtual

    return lista

main()

# creditos, 50% patro; 40% jota e 10% sammya.
