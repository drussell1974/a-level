class PostOrderSearchTree:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = PostOrderSearchTree(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = PostOrderSearchTree(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def print_tree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

    def search(self, root):
        res = []
        if root:
            res = self.search(root.left)
            res = res + self.search(root.right)
            res.append(root.data)
        return res


# TESTS
if __name__ == '__main__':
    root = PostOrderSearchTree(27)
    root.insert(14)
    root.insert(35)
    root.insert(10)
    root.insert(19)
    root.insert(31)
    root.insert(42)
    # test search
    print(root.search(root))
    # test print tree
    root.print_tree()
