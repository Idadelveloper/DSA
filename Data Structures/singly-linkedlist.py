class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
        

class SinglyLL:
    def __init__(self):
        self.head = Node()
        self.tail = self.head
        self.size = 1

    def insertFirst(self, value):
        if self.head.value == None:
            self.head.value = value
            self.tail.value = value
        else:
            node = Node()
            node.value = value
            node.next = self.head
            self.head = node
            self.size += 1 

    def insertLast(self, value):
        if self.head.value == None and self.size == 1:
            self.insertFirst(value)
        else:
            node = Node()
            node.value = value
            self.tail.next = node
            self.tail = node
            self.size += 1

    def insert(self, value, index):
        if index > self.size:
            print("index out of range")
            return
        if index == 0:
            self.insertFirst(value)
            return
        if index == self.size:
            self.insertLast(value)
            return
        temp = self.head
        i = 1
        while i < index:
            temp = temp.next
            i += 1
        node = Node()
        node.value = value
        node.next = temp.next
        temp.next = node
        self.size += 1

    def deleteFirst(self):
        val = self.head.value
        self.head = self.head.next
        self.size -= 1
        return val

    def deleteLast(self):
        if self.size <= 1:
            return self.deleteFirst()
        temp = self.head
        count = 1
        while count < self.size:
            temp = temp.next
            count += 1
        val = self.tail.value
        self.tail = temp
        self.tail.next = None
        self.size -= 1
        return val

    def delete(self, index):
        if index == 0:
            return self.deleteFirst()
        if index == self.size - 1:
            return self.deleteLast()
        if index > self.size -1:
            print("index out of range")
            return
        if index == 0:
            self.head = self.head.next
            self.size -= 1
        i = 1
        temp = self.head
        while i < index:
            temp = temp.next
            i += 1
        val = temp.value
        temp.next = temp.next.next
        self.size -= 1
        return val
    

    def display(self):
        temp = self.head
        final = ""
        while temp != None:
            # print(str(temp.value) + "-->")
            final = final + str(temp.value) + "-->"
            temp = temp.next
        final += "END"
        print(final)


singlyll = SinglyLL()
singlyll.display()
singlyll.insertFirst(3)
singlyll.display()
singlyll.insertFirst(7)
singlyll.display()
singlyll.insertFirst(10)
singlyll.display()
singlyll.insertLast(8)
singlyll.display()
singlyll.insertLast(25)
singlyll.display()
singlyll.insertLast(17)
singlyll.display()
singlyll.insertFirst(1)
singlyll.display()
singlyll.insert(38, 2)
singlyll.display()
singlyll.insert(44, 6)
singlyll.display()
singlyll.delete(8)
singlyll.display()
singlyll.deleteFirst()
singlyll.display()
singlyll.deleteLast()
singlyll.display()
print(singlyll.deleteLast())
singlyll.delete(0)

print(singlyll.size)
singlyll.display()
