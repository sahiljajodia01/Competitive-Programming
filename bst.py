class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root:
            self._insert(self.root, val)
        else:
            self.root = Node(val)

    def _insert(self, root, val):
        while True:
            if val < root.val:
                if root.left:
                    root = root.left
                else:
                    root.left = Node(val)
                    break
            else:
                if root.right:
                    root = root.right
                else:
                    root.right = Node(val)
                    break

    
    def print_tree(self):
        self._print_tree(self.root)
    
    def _print_tree(self, root):
        if root:
            self._print_tree(root.left)
            print(root.val, " ")
            self._print_tree(root.right)

tree = BST()

tree.insert(5)
tree.insert(4)
tree.insert(10)
tree.insert(2)
tree.insert(3)
tree.insert(25)

tree.print_tree()
