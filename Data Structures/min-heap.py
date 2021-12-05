class MinHeap:
    """
    Implementation of minimum heap using arrays
    """
    def __init__(self, capacity):
        self.storage = [0] * capacity
        self.capacity = capacity
        self.size = 0

    def getParentIndex(self, index):
        return (index-1)//2
    
    def getLeftChildIndex(self, index):
        return 2 * index + 1
    
    def getRightChildIndex(self, index):
        return 2 * index + 1

    def hasParent(self, index):
        return self.getParentIndex(index) >= 0

    def hasLeftChild(self, index):
        return self.getLeftChildIndex(index) < self.size

    def hasRightChildIndex(self, index):
        return self.getRightChildIndex(index) < self.size

    def parent(self, index):
        return self.storage[self.getParentIndex(index)]

    def leftChild(self, index):
        return self.storage[self.getLeftChildIndex(index)]

    def rightChild(self, index):
        return self.storage[self.getRightChildIndex(index)]

    def isFull(self):
        return self.size == self.capacity

    def swap(self, index1, index2):
        temp = self.storage[index1]
        self.storage[index1] = self.storage[index2]
        self.storage[index2] = temp

    def heapifyUp(self, index):
        if self.hasParent(index) and self.parent(index) > self.storage[index]:
            self.swap(self.getParentIndex(index), index)
            self.heapifyUp(self.getParentIndex(index))

    def insert(self, data):
        if self.isFull():
            raise("Heap is full")
        self.storage[self.size] = data
        self.size += 1
        self.heapifyUp(self.size-1)

    def heapifyDown(self, index):
        smallest = index
        if self.hasLeftChild(index) and self.storage[smallest] > self.leftChild(index):
            smallest = self.getLeftChildIndex(index)
        if self.hasRightChildIndex(index) and self.rightChild(index) > self.leftChild(index):
            smallest = self.getRightChildIndex(index)
        if smallest != index:
            self.swap(index, smallest)
            self.heapifyDown(smallest)

    def removeMin(self):
        if self.size == 0:
            raise("Empty Heap")
        data = self.storage[0]
        self.storage[0] = self.storage[self.size - 1]
        self.size -= 1
        self.heapifyDown(0)
        return data


# Test
my_heap = MinHeap(10)
my_heap.insert(5)
my_heap.insert(20)
my_heap.insert(15)
print(my_heap.size)
my_heap.insert(24)
my_heap.insert(6)
my_heap.insert(0)
print(my_heap.size)
print(my_heap.removeMin())
print(my_heap.size)
print(my_heap.removeMin())
print(my_heap.size)
