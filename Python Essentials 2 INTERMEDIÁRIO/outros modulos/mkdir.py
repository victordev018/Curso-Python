# A função mkdir cria uma diretoria no caminho especificado. 
# a funcção faz parte do módulo os, temos de importa-lo.

import os
os.mkdir("new past")  #criando uma nova pasta

# A função mkdir cria uma diretoria no caminho especificado. A função listdir devolve 
# uma lista contendo os nomes dos ficheiros e diretorias que se encontram no caminho 
# passado como um argumento.
print(os.listdir()) # listdir() devolve uma lista de nomes de ficheiros naquele caminho 

# A função makedirs permite a criação de diretoria recursiva, o que significa que todas as 
# diretorias no caminho serão criadas.

os.makedirs("pasta1/pasta2")
# os.chdir("pasta 1")
print(os.listdir())

print("caminho atual: ", os.getcwd()) # getcwd, retorna o caminho atual

# para remover diretórios:
# rmdir() -> remove uma diretoria com um caminho específico:
# removedirs() -> remove uma diretoria e suas subdiretorias:
print("removendo a pasta 'new past': ", os.rmdir("new past"))
print("Removendo 'pasta1' e sua subpasta 'pasta2': ", os.removedirs("pasta1/pasta2"))
print(os.listdir())