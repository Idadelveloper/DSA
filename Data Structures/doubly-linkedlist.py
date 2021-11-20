class Node:
    def __init__(self, value=None, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


class DoublyLL:
    def __init__(self):
        node = Node()
        self.head = node
        self.tail = node
        self.size = 1
    
    def insert_at_beginning(self, value):
        if self.head.next == None:
            self.head.value = value
            self.tail.value = value
            return
        node = Node()
        node.value = value
        self.head.prev = node
        node.next = self.head
        self.head = node
        self.size += 1

    def insert_at_end(self, value):
        if self.head.value == None and self.size <= 1:
            self.tail.value = value
            self.head.value = value
            return
        node = Node()
        node.value = value
        self.tail.next = node
        node.prev = self.tail
        self.tail = node
        self.size += 1

    def insert(self, value, index):
        if index > self.size:
            print("Index out of range")
            return
        if index == 0:
            self.insert_at_beginning(value)
            return
        if index == self.size:
            self.insert_at_end(value)
            return
        itr = self.head
        count = 0
        while itr != None:
            if count == index-1:
                break
            itr = itr.next
            count += 1
        node = Node()
        node.value = value
        node.prev = itr
        node.next = itr.next
        itr.next = node
        self.size += 1

    def deleteFirst(self):
        deleted = self.head.value
        if self.size == 1:
            self.head = None
            self.tail = None
            self.size -= 1
            return deleted
        self.head = self.head.next
        self.prev = None
        self.size -= 1
        return deleted

    def deleteLast(self):
        deleted = self.head.value
        if self.size == 1:
            self.head = None
            self.tail = None
            self.size -= 1
            return deleted
        self.tail = self.tail.prev
        self.tail.next = None
        self.size -= 1
        return deleted

    def print_list(self):
        itr = self.head
        result = ""
        while itr != None:
            result = result + str(itr.value) + " --> "
            itr = itr.next
        result += "END"
        print(result)
    
    def print_rev(self):
        """
            Reverse print the linked list
        """
        itr = self.tail
        result = ""
        while itr != None:
            result = result + str(itr.value) + " --> "
            itr = itr.prev
        result += "END"
        print(result)


doublyll = DoublyLL()
doublyll.print_list()
doublyll.insert_at_beginning(5)
doublyll.print_list()
doublyll.insert_at_end(6)
doublyll.print_list()
doublyll.insert_at_beginning(9)
doublyll.print_list()
print("Next insert 45 at index 2")
doublyll.insert(45, 2)
doublyll.print_list()
print("Next insert 13 at index 0")
doublyll.insert(13, 0)
doublyll.print_list()
print("Next insert 16 at index 5")
doublyll.insert(16, 5)
doublyll.print_list()
print("Next delete first item")
print(doublyll.deleteFirst())
doublyll.print_list()
print("Next delete last item")
print(doublyll.deleteLast())
doublyll.print_list()
print("Next print list size")
print(doublyll.size)

            


