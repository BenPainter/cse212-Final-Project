class Tree:
    class Node:

        def __init__(self, data, price):

            self.data = data
            self.price = price
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, data, price):
        if self.root is None:
            self.root = Tree.Node(data.lower(), price)
        else:
            self._insert(data, self.root, price) 

    def _insert(self, data, node, price):
        if data < node.data:
            if node.left is None:
                node.left = Tree.Node(data.lower(), price)
            else:
                self._insert(data, node.left, price)
        else:
            if node.right is None:
                node.right = Tree.Node(data.lower(), price)
            else:
                self._insert(data, node.right, price)

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
            yield (node.data, node.price)
            yield from self.traverse_forward(node.right)

tree = Tree()
tree.insert("Granite", 10)
tree.insert("Diorite", 50)
tree.insert("Sandstone", 5)
tree.insert("Limestone", 2)
tree.insert("Slate", 7)
tree.insert("Obsidian", 21)
tree.insert("Chalk", 1)
tree.insert("Coal", 4)
tree.insert("Pumice", 2)
tree.insert("Basalt", 5)

print("*******************************")
print("The list of rocks and their values")
for x in tree:
    print(x)

