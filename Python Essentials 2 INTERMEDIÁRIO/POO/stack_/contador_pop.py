class Stack:
    def __init__(self):
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val


class CountingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__cont_pop = 0

    def get_counter(self):
        return self.__cont_pop

    def pop(self):
        value = Stack.pop
        self.__cont_pop += 1
        return value
	

stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()
print("quantidade de pop: ",stk.get_counter())