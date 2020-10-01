class Node:
    def __init__(self, data, left=None, right=None):
        self.left = left
        self.right = right
        self.data = data

    def inorder(self):
        if self.left:
            self.left.inorder()

        print(self.data)

        if self.right:
            self.right.inorder()

    def preorder(self):
        print(self.data)

        if self.left:
            self.left.inorder()

        if self.right:
            self.right.inorder()

    def postorder(self):
        if self.left:
            self.left.inorder()

        if self.right:
            self.right.inorder()

        print(self.data)


def construct(node, pyramid):
    for level, row in enumerate(pyramid[:-1]):
        for index, value in enumerate(row):
            node.left = Node(pyramid[level + 1][index])
            node.right = Node(pyramid[level + 1][index + 1])
            construct(node.left, pyramid[1:])
            construct(node.right, pyramid[1:])
    return node


n = construct(Node(75), [[75], [95, 64], [17, 47, 82]])
print("INORDER")
n.inorder()
print("POSTORDER")
n.postorder()
print("PREORDER")
n.preorder()
