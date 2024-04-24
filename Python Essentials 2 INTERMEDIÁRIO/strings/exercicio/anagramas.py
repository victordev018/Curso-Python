# verificar se duas palavras formam um anagrana:
word1 = input("word 1 : ")
word2 = input("word 2 : ")
qtd_true = 0

for letra in word1:
    if letra in word2:
        qtd_true += 1

if qtd_true == len(word1):
    print("Is a anagram")
else:
    print("Is a not anagtram...")