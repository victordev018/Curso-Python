# ord(), serve para saber o valor do code point ASCII/UNICODE de um caratere específico
# obs: a função necessita-se necessariamente de uma strfing de um único caractere

print("point code 'a': ",ord('a')) # cod: 97
print("code point de 'A': ",ord('A')) # cod: 65

#chr(), faz o inverso de ord(), passa como parãmetro o valor do code-point e será retornado o caractere
print("caractere do code point '97': ", chr(97))  # caractere: 'a'
