# Check if a target element is in a binary tree

class BinaryTreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# def treeIncludes(root, target):
#     # breadth first search
#     if root == None:
#         return False
#     queue = [root]
#     while len(queue) > 0:
#         current = queue.pop(0)
#         if current.value == target:
#             return True
#         else:
#             return False
#         if current.left:
#             queue.append(current.left)
#         if current.right:
#             queue.append(current.right)
#     return False


def treeIncludesDF(root, target):
    # depth first search recursive
    if root == None:
        return False
    if root.value == target:
        return True
    if treeIncludesDF(root.left, target) or treeIncludesDF(root.right, target):
        return True
    


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

# print(treeIncludes(a, "F"))
print(treeIncludesDF(a, "F"))
