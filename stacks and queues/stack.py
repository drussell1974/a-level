from arrays import StaticArray 
# last in last out
class Stack(StaticArray):
    def __init__(self, fixed_size):
        # initialise the pointer
        self.pointer = -1
        # create a static array
        super().__init__(fixed_size)
        
        
    def pop(self):
        """ get the item and remove it from the top of the stack """
        # get the item before removing it
        item = self.get(self.pointer)
        self.remove(self.pointer)
        # decrement pointer
        self.pointer = self.pointer - 1
        
        return item
         
         
    def push(self, item):
        """ add an item to the top of stack """
        # increment pointer and put the item on top of the stack
        self.pointer = self.pointer + 1
        self.set(self.pointer, item)

    
if __name__ == '__main__':
    """ TESTS """
    q = Stack(4)
    print("Initial stack:", q)

    q.push("I")
    q.push("am")
    q.push("the")
    print("Populated:", q, ",Count:", len(q))
    assert len(q) == 3, "length should be 3"

    item = q.pop()
    assert item == "the", "pop() should dequeue 'the'"
    assert len(q) == 2, "length should be 2"

    item = q.pop()
    assert item == "am", "pop() should dequeue 'am'"
    assert len(q) == 1, "length should be 1"

    q.push("one")
    print("Add another item 'one':", q, ",Count:", len(q))
    assert len(q) == 2, "length should be 2"

    item = q.pop()
    print("Remove item:", q, ",Count:", len(q))
    assert len(q) == 1, "length should be 1"
    assert item == "one", "pop() should dequeue 'one' (the last item pushed)"
