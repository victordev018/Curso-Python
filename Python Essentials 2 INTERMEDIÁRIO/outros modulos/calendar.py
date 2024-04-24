# vamos usar o módulo calendar para exibir o calendário de um determinado ano:
# import calendar
# calendar.prcal(2024) # calendario do ano de 2024

# import calendar
# print(calendar.month(2020, 11))

# o método weekday(), devolve o número do dia da semana que vai cair aquela data 
import calendar
print(calendar.weekday(2020, 12, 24))

# para verificar de um ano é bissexto, o calendat fornece uma função chamada isleap
# isleap devolve True se for bissexto ou False, caso contrário.
print(calendar.isleap(2020)) # True