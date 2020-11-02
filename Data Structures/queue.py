class Queue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.input = [None] * self.max_size
        self.size = 0
        self.front = 0
        self.rear = -1


    def is_empty(self):
        if self.max_size == 0:
            return True


    def front(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.input[self.front]


    def rear(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.input[self.rear]


    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        answer = self.input[self.front]
        self.input[self.front] = None
        self.front = (self.front + 1) % self.max_size
        self.max_size -= 1
        self.rear -= 1
        return answer


    def enqueue(self, item):
        self.item = item
        if self.max_size == 0:
            raise Exception("Queue is full")
        self.rear += 1
        self.max_size += 1
        self.input[self.rear] = self.item
        return self.input 


# Example
my_queue = Queue(5)
print(my_queue.is_empty())
print(my_queue.enqueue(1))
print(my_queue.enqueue(2))
print(my_queue.enqueue(5))
print(my_queue.dequeue())
print(my_queue.enqueue(3))
print(my_queue.enqueue(4))
print(my_queue.enqueue(5))
print(my_queue.dequeue())
print(my_queue)
