class Tree:
    class Node:

        def __init__(self, data):

            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Tree.Node(data.lower())
        else:
            self._insert(data, self.root) 

    def _insert(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = Tree.Node(data.lower())
            else:
                self._insert(data, node.left)
        else:
            if node.right is None:
                node.right = Tree.Node(data.lower())
            else:
                self._insert(data, node.right)

    def _contains(self, data):
        return self.contains(data, self.root)

    def contains(self, data, node):
        if node is None:
            return False
        elif data == node.data:
            return True
        elif data < node.data:
            return self.contains(data, node.left)
        else:
            return self.contains(data, node.right)
         
    def __iter__(self):
        yield from self.traverse_forward(self.root) 
        
    def traverse_forward(self, node):
        if node is not None:
            yield from self.traverse_forward(node.left)
            yield node.data
            yield from self.traverse_forward(node.right)

tree = Tree()
"""
Add rocks and their values
"""

print("*******************************")
print("The list of rocks and their values")
for x in tree:
    print(x)

