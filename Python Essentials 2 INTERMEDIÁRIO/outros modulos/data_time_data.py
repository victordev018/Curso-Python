# Uma das classes fornecidas pelo módulo datetime é uma classe chamada date. Os objetos desta 
# classe representam uma data que consiste no ano, mês e dia. 

from datetime import date

today = date.today()  # today(), fornece a data atual

print("Today: ", today)
print("Year: ", today.year)  # fornece o ano atual
print("Month: ", today.month)  # fornece o mês atual
print("Day: ", today.day)  # fornece o dia atual

# Para criar um objeto date , deve passar os parâmetros de ano, mês e dia como se segue:
meu_aniversário = date(2005, 6, 24)
print("\nmeu aniversário: ", meu_aniversário)

# O módulo datetime fornece vários métodos para criar um objeto date . Um deles é o método fromisoformat,
# que tem uma data no formato YYYY-MM-DD em conformidade com a norma ISO 8601.

from datetime import date

d = date.fromisoformat('2019-11-04')
print("date from isoformat: ",d)

# Por vezes pode ser necessário substituir o ano, mês, ou dia por um valor diferente. Não se pode fazer
# isto com os atributos de ano, mês e dia porque são apenas de leitura. Neste caso, pode utilizar o método 
# denominado replace.

aniversario = date(2004, 4, 23)
print("Aniversário 1: ", aniversario)
aniversario = aniversario.replace(year=2005, month=6, day=24)
print("Aniversário 2: ", aniversario)

# Um dos métodos mais úteis que facilita o trabalho com datas é o método chamado weekday. Ele devolve o dia da 
# semana como um número inteiro, onde 0 é segunda-feira e 6 é domingo.

def verificarDiaSemana(dia): # função para retornar o dia da semana por extenso
    if dia == 0:
        return "segunda"
    elif dia == 1:
        return "terça"
    elif dia == 2:
        return "quarta"
    elif dia == 3:
        return "quinta"
    elif dia == 4:
        return "sexta"
    elif dia == 5:
        return "sábado"
    else:
        return "domingo"

diaSemana = date.today().weekday() # dia da semana da data atual:
print("dia da semana: ",verificarDiaSemana(diaSemana))