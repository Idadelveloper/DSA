


class LinkedListStack:
    """
    Implementation of stack using linked list
    """
    class Node:
        def __init__(self, item, next_node):
        self.item = item
        self.next_node = next_node


    def __init__(self):
        self.head = None
        self.size = 0


    def is_empty(self):
        if self.size == 0:
            return True


    def push(self, new_node):
        self.new_node = new_node
        self.head = self.Node(new_node, self.head)
        self.size += 1


    def top(self):
        if self.size == 0:
            raise Exception("Stack is empty")
        return self.head.element


    def pop(self):
        if self.size == 0:
            raise Exception("Stack is empty")
        answer = self.head.item
        self.head = self.head.next
        self.size -= 1
        return answer
