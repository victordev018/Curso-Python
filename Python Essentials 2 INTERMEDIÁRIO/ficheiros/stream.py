# com streams ou handles, é possível implementar o processo de acesso a qualquer ficheiro
# A operação de conectar o stream com um ficheiro chama-se abrir o ficheiro(open), enquanto que 
# desconectar esta ligação chama-se fechar o ficheiro(close).

# Existem três modos básicos usados para abrir o stream:

# read mode (modo de leitura): um stream aberto neste modo permite apenas operações de leitura; 
# tentar escrever no stream causará uma exceção (nomeada UnsupportedOperation, que herda OSError e ValueError, 
# e vem do io módulo);

# write mode (modo de escrita): um stream aberto neste modo permite apenas operações de escrita; tentar ler o 
# stream causará a exceção mencionada acima;

# update mode (modo de atualização): um stream aberto neste modo permite tanto escritas como leituras.

# A abertura do stream é realizada por uma função que pode ser invocada da seguinte forma:

stream = open("file", mode = 'r', encoding = None)

# or 
stream = open("file")


# Vamos analisá-la:

# o nome da função (open) fala por si; se a abertura for bem sucedida, a função devolve um objeto de stream;
# caso contrário, é levantada uma exceção (por exemplo, FileNotFoundError se o ficheiro que vai ler não existir);

# o primeiro parâmetro da função (file) especifica o nome do ficheiro a ser associado ao stream;

# o segundo parâmetro (mode) especifica o modo aberto utilizado para o stream; é uma string cheia de carateres,
# e cada um deles tem o seu significado especial (mais detalhes em breve);

# o terceiro parâmetro (encoding) especifica o tipo de codificação (por exemplo, UTF-8 quando se trabalha com 
# ficheiros de texto)

# a abertura deve ser a primeira operação realizada no stream.
# Nota: o modo e os argumentos de codificação podem ser omitidos - os seus valores por defeito são então assumidos.
# O modo de abertura padrão é a leitura em modo de texto, enquanto que a codificação padrão depende da plataforma 
# utilizada.