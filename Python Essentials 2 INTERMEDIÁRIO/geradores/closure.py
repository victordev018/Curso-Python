# a claure acontece quando retornamos uma função dentro de outraclosure é uma técnica 
# que permite o armazenamento de valores apesar do facto de o contexto em que foram criados já não existir.

def outer(par):
    loc = par

    def inner():
        return loc
    return inner


var = 1
fun = outer(var)
print(fun())

# A função devolvida durante a invocação outer() é um closure.
