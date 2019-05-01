from SearchTree import SearchTree

class PreOrderSearchTree(SearchTree):

    def __init__(self, data):
        super().__init__(data)

    def search(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.search(root.left)
            res = res + self.search(root.right)
        return res

# TESTS
if __name__ == '__main__':
    root = PreOrderSearchTree(27)
    root.insert(14)
    root.insert(35)
    root.insert(10)
    root.insert(19)
    root.insert(31)
    root.insert(42)
    print(root.search(root))
