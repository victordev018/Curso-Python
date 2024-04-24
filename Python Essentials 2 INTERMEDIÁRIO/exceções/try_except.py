# uma das formas preferidas do python, de everificação é o Try-except:

valu1 = int(input("value 1: "))
valu2 = int(input("value 2: "))

try:
    print(valu1/valu2)
except:  # este é executado quando o try da errado..
    print('Não é possivel efetuar a operação...'
          
# Uma exceção é um evento na execução de um programa causado por uma situação anormal. 
# A exceção deve ser tratada para evitar a terminação do programa. A parte do seu código 
# que é suspeita de ser a origem da exceção deve ser colocada dentro do ramo try .
# Quando a exceção acontece, a execução do código não é terminada, mas em vez disso salta 
# para o ramo except . Este é o local onde deve ter lugar o tratamento da exceção. O esquema 
# geral de tal construção parece-se com o seguinte: