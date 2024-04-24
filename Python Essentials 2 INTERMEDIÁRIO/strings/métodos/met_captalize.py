# o método capitalize: se o primeiro elemento da string for uma letra, 
# será convertido para maiúsculas, todas as letras restantes da string 
# serão convertidas em minúsculas.

print('aBcD'.capitalize())

# outros testes:
print("\nAlpha".capitalize()) # permanece como esta
print('ALPHA'.capitalize()) # Alpha
print(' Alpha'.capitalize()) # alpha
print('123'.capitalize())  # 123
print("αβγδ".capitalize())  # Aβγδ
