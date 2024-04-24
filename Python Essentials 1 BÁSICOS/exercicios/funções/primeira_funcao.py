# declaração defunções nao parametizadas

print("\nFunção não paramentrizada: ")
def message():
    print("Enter a value: ")

message()
a = int(input())
message()
b = int(input())
message()
c = int(input())

# declaração de funções parametrizadas:
print("\nFunção parametrizada")
def ShowNUmber(number):
    print("\nYour number: ", number)

value = int(input("\nEnter a value: "))
ShowNUmber(value)