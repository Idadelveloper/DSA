# Depth First Search Traversal of a Binary Tree

class BinaryTreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def depthFirstValues(root):
    """
    Depth First Search traversal of a binary tree using a loop which returns array of values
    """
    if root == None:
        return []

    result = []
    stack = [root]
    while len(stack) > 0:
        current = stack.pop()
        result.append(current.value)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    return result

def depthFirstValuesRecur(root):
    """
    Depth First Search Binary Tree traversal using recursion
    """
    if root is None:
        return []
    leftValues = depthFirstValuesRecur(root.left)
    rightValues = depthFirstValuesRecur(root.right)
    result = [root.value]
    result.extend(leftValues)
    result.extend(rightValues)
    return result


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



print(depthFirstValues(a))
# result = ['A', 'B', 'D', 'E', 'C', 'F']
print(depthFirstValuesRecur(a))
# result = ['A', 'B', 'D', 'E', 'C', 'F']
