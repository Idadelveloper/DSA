import math


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def maxPathSum(root):
  """
  Maximum sum of path from leaf to root
  """
    if root == None:
        return -math.inf
    if root.left == None and root.right == None:
        return root.value

    maxChildPathSum = max(maxPathSum(root.left), maxPathSum(root.right))
    return root.value + maxChildPathSum


a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(-2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

print(maxPathSum(a))
