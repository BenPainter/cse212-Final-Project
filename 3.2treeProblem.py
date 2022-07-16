class FamilyTree:
    class Node:

        def __init__(self, data):

            self.data = data
            self.mother = None
            self.father = None

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = FamilyTree.Node(data.lower())
        else:
            self._insert(data, self.root) 

    def _insert(self, data, node):
        if data < node.data:
            if node.mother is None:
                node.mother = FamilyTree.Node(data.lower())
            else:
                self._insert(data, node.mother)
        else:
            if node.father is None:
                node.father = FamilyTree.Node(data.lower())
            else:
                self._insert(data, node.father)
         
    def __iter__(self):
        yield from self.traverse_forward(self.root) 
        
    def traverse_forward(self, node):
        if node is not None:
            yield node.data
            yield from self.traverse_forward(node.mother)
            yield from self.traverse_forward(node.father)

tree = FamilyTree()
tree.insert("3 - Mr. Smith")
"""
Create Mr. Smith's Family Tree
Make sure you add them in the correct order
"""
for x in tree:
    print (x)
    """
    This should be the order when printed
    mr. smith
    mrs. smith
    bob
    mr. smith senior
    mr. smith senior's mom
    mr. smith senior's dad
    """


