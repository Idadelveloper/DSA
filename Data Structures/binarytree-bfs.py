class BinaryTreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def breadthFirstValues(root):
    """
    Breadth First Search traversal from left to right
    """
    if root == None:
        return []

    values = []
    queue = [root]

    while len(queue) > 0:
        current = queue.pop(0)
        values.append(current.value)
        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)
    return values

a = BinaryTreeNode("A")
b = BinaryTreeNode("B")
c = BinaryTreeNode("C")
d = BinaryTreeNode("D")
e = BinaryTreeNode("E")
f = BinaryTreeNode("F")

a.left = b # the root node
a.right = c
b.left = d
b.right = e
c.right = f


    #       A
    #     /   \
    #    B     C 
    #   / \     \
    #  D   E     F

print(breadthFirstValues(a))
# result = ['A', 'B', 'C', 'D', 'E', 'F']
        
