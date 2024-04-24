class Timer:
    string_hora = ""
    def __init__(self, h=0,m=0,s=0):
        self.__hora = h
        self.__minute = m
        self.__second = s
        
    def __str__(self):
        return f'{self.__hora}:{self.__minute}:{self.__second}'


    def next_second(self):
       self.__second += 1
       
       if self.__second > 59:
           self.__second = 00
           self.__minute += 1
       
       if self.__minute > 50:
           self.__minute = 00
           self.__hora += 1
        
       if self.__hora > 23:
           self.__hora == 00
    
       

    def prev_second(self):
        pass

# __str__, retorna uma string sobre a clsse, mas podemos modifica-la
# para fazer um retorno como desejarmos
timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
# timer.prev_second()
# print(timer)