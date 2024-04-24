# vamos construir um gerador:

def fun(n):
    for i in range(n):
        yield i  # a keyword yield, não perde o estado da função(não partirá do zero a cada invocação).

for i in fun(5):
    print("elemento: ",i)


# em forma de lista:
l = [i for i in fun(5)]
print("Lista: ",l)

# A função list() pode transformar uma série de invocações de geradores subsequentes numa lista real:

t = list(fun(4))
print("List: ", t)