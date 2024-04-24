# r modo aberto: read
# o stream será aberto em read mode (modo de leitura);
# o ficheiro associado ao stream tem de existir e tem de ser legível, caso contrário a função open() 
# levanta uma exceção.

# w modo aberto: write
# o stream será aberto em write mode (modo de escrita);
# o ficheiro associado ao stream não precisa de existir; se não existir, será criado; se existir, 
# será truncado até ao comprimento de zero (apagado); se a criação não for possível (por exemplo, 
# devido às permissões do sistema) a função open() levanta uma exceção.

# a modo aberto: append
# o stream será aberto em append mode (modo anexo);
# o ficheiro associado ao stream não precisa de existir; se não existir, será criado; se existir, 
# a cabeça de gravação virtual será colocada no fim do ficheiro (o conteúdo anterior do ficheiro 
# permanece intocado).

# r+ modo aberto: read and update
# o stream será aberto em read and update mode (modo de leitura e atualização);
# o ficheiro associado ao stream tem de existir e tem de ser gravável, caso contrário a função open()
#  levanta uma exceção;
# tanto as operações de leitura como de escrita são permitidas para o stream.

# w+ modo aberto: write and update
# o stream será aberto em write and update mode (modo de gravação e atualização);
# o ficheiro associado ao stream não precisa de existir; se não existir, será criado; o conteúdo anterior 
# do ficheiro permanece intocado;
# tanto as operações de leitura como de escrita são permitidas para o stream.

# Também se pode abrir um ficheiro para a sua criação exclusiva. Pode fazer isto usando o x modo aberto. 
# Se o ficheiro já existir, a função open() irá levantar uma exceção.

# lendo um ficheiro e tratando a exceção:
try:
    stream = open("C:\\JV past\\Labiras\\curso python\\Python Essentials 2 INTERMEDIÁRIO\\ficheiros\\teste.txt", "rt")
    # processing  goes here
    print(stream)
except Exception as exc:
    print("Cannot open file:", exc)

stream2 = open("C:\\JV past\\Labiras\\curso python\\Python Essentials 2 INTERMEDIÁRIO\\ficheiros\\teste.txt", "rt")
print("Read: ", stream2.read())  # o método read() faz a leitura do arquivo txt previamente aberto.

# para tratarmos o ficheiro a partir daas linhas , utilizamos o método readline():

# A classe readlines() , quando invocado sem argumentos, tenta ler todo o conteúdo do ficheiro, e devolve 
# uma lista de strings, um elemento por linha de ficheiro.
