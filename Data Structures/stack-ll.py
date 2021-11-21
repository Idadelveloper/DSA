# Implementation of a stack using linked list

class Node:
    def __init__(self, value=None, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


class Stack:
    def __init__(self, max_size=50):
        """"
            Initializes stack with a default maximum size of 50
        """
        node = Node()
        self.top = node
        self.max_size = max_size
        self.size = 1

    def isEmpty(self):
        if self.top.prev == None and self.top.value == None:
            return True

    def push(self, value):
        if self.isEmpty():
            self.top.value = value
            return
        if self.max_size == self.size:
            print("Stack is full")
            return
        node = Node()
        node.value = value
        node.prev = self.top
        self.top.next = node
        self.top = node
        self.size += 1

    def pop(self):
        if self.size == 1:
            self.top.value = None
            self.top.next = None
            self.top.prev = None
        popped = self.top.value
        self.top = self.top.prev
        self.top.next = None
        self.size -= 1
        return popped

    def print_stack(self):
        itr = self.top
        final = "TOP --> "
        while itr != None:
            final = final + str(itr.value) + " --> "
            itr = itr.prev
        final += "BOTTOM"
        print(final)

        
    

# Test
my_stack = Stack()
my_stack.print_stack()
my_stack.push(2)
my_stack.push(13)
my_stack.push(45)
my_stack.push(64)
my_stack.print_stack()
print(my_stack.size)
print(my_stack.pop())
my_stack.print_stack()
print(my_stack.size)
print(my_stack.top.value)
