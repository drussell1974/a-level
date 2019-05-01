from SearchTree import SearchTree

class PostOrderSearchTree(SearchTree):

    def __init__(self, data):
        super().__init__(data)
        

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
    print(root.search(root))
