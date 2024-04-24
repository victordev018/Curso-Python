# stack processual // pilhas

stack =  []

# função push - para adicionar o=um novo valor no topo da stack
def push(value): 
    stack.append(value)

# função pop - para tirar o útimo valor adicionado:
def pop():
    value = stack[-1]  # "seguro" o útimo valor
    del stack[-1]      # removo o útimo valor da stack
    return value       # retorno o valor que foi guardado

# ato de empilhar:
push(3)
push(2)
push(1)

# seguindo a lógica, 1 está no topo, 2 no meio, e 3 na base

# ato de tirar
print(pop())   #1
print(pop())   #2
print(pop())   #3
