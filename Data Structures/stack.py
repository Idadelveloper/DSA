class Stack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.input = []


    def is_full(self):
        if len(self.input) == self.max_size:
            return True
        else:
            return False


    def is_empty(self):
        if len(self.input) == 0:
            return True
        else:
            return False


    def push(self, item):
        self.item = item
        if len(self.input) < self.max_size:
            self.input.append(self.item)
            return self.input
        else:
            print("Stack is full")


    def pop(self):
        if len(self.input) == 0:
            print("Stack is empty")
        else:
            self.input.pop()
            return self.input


#Example
my_stack = Stack(5)
print(my_stack.is_full())
print(my_stack.push(1))
print(my_stack.push(2))
print(my_stack.push(5))
print(my_stack.pop())
print(my_stack.push(3))
print(my_stack.push(4))
print(my_stack.push(5))
my_stack.push(6)
print(my_stack.is_full())
