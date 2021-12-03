class BinaryTreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


import math


def treeMinValue(root):
    smallest = math.inf
    stack = [root]

    while len(stack) > 0:
        current = stack.pop()
        if current.value < smallest:
            smallest = current.value

        if current.left != None:
            stack.append(current.left)
        if current.right != None:
            stack.append(current.current.right)

    return smallest


a = BinaryTreeNode(2)
b = BinaryTreeNode(5)
c = BinaryTreeNode(12)
d = BinaryTreeNode(17)
e = BinaryTreeNode(8)
f = BinaryTreeNode(45)

a.left = b # the root node
a.right = c
b.left = d
b.right = e
c.right = f

print(treeMinValue(a))
