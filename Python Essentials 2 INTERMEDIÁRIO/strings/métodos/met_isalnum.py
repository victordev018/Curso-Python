# o método sem parâmetro isalnum(), verifica se a string possui só digitos(num) ou caracteres(letras)
# se sim retorna True:
# outro caso retrona False
print("\nIsalnum()")
print("joao_dev".isalnum())       #False, '_'
print("18932".isalnum())          #True
print("".isalnum())               #False, "" vazio
print("@".isalnum())              #False, "@"

# a classe, isaalpha(), esta interessada apenas em letras
print("\nIsalpha()")
print("jbde3".isalpha())          #False, "3"

# a clase, isdigi(), esta interessada apenas em números
print("\nIsdigit()")
print("1873".isdigit())           #True

# A classe islower() é uma variante picuinhas do isalpha() - aceita apenas letras minúsculas.
print("\nIslower()")
print("akhdui".islower())         #True

# A clase issapce(), identifica apenas espaços:
print("\nISspace()")
print("ad ad".isspace())          #False

# A classe isupper() é a versão maiúscula do islower() - concentra-se apenas em letras maiúsculas.
print("\nIsupper()")
print("GDTSU".isupper())         #True