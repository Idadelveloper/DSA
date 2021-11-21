# Implementation of the Queue data structure using Doubly Linked List

class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    
class Queue:
    def __init__(self, max_size=50):
        '''
            Initializes queue with a default maximum size of 50
        '''
        node = Node()
        self.front = node
        self.rear = node
        self.max_size = max_size
        self.size = 1

    def enqueue(self, data):
        if self.size == self.max_size:
            print("Queue is full")
            return
        if self.front.data == None and self.size == 1:
            self.front.data = data
            self.rear.data = data
            return
        node = Node()
        node.data = data
        node.next = self.rear
        self.rear.prev = node
        self.rear = node
        self.size += 1

    def dequeue(self):
        if self.size == 1:
            self.front.data = None
            self.rear.data = None
            return
        popped = self.front.data
        self.front = self.front.prev
        self.front.next = None
        self.size -= 1
        return popped

    def display(self):
        itr = self.rear
        final = "REAR --> "
        while itr is not None:
            final = final + str(itr.data) + " --> "
            itr = itr.next
        final += "FRONT"
        print(final)


# Test
my_queue = Queue()
my_queue.display()
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.enqueue(4)
my_queue.enqueue(5)
my_queue.display()
print(my_queue.size)
print(my_queue.dequeue())
my_queue.display()
print(my_queue.size)

