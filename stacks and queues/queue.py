from arrays import StaticArray
# First in First out
class Queue(StaticArray):
    def __init__(self, fixed_size):
        # initialise front of queue
        self.head_pointer = -1
        # initialise value for back of queue
        self.tail_pointer = -1
        # create a static array
        super().__init__(fixed_size)
        
        
    def pop(self):
        """ Dequeue and return the item """
        # get the item from the top of the queue
        # increment the head pointer and get the item before removing
        self.head_pointer = self.head_pointer + 1
        item = self._get(self.head_pointer)
        self._remove(self.head_pointer)
        
        return item
    
    
    def push(self, item):
        """ Enqueue to bottom of list """
        # increment tail pointer and put the item at the back of the queue
        self.tail_pointer = self.tail_pointer + 1
        self._put(self.tail_pointer, item)

    
if __name__ == '__main__':
    """ TESTS """
    q = Queue(4)
    print("Initial queue:", q)

    q.push("I")
    q.push("am")
    q.push("the")
    print("Populated:", q)
    assert len(q) == 3, "length should be 3"

    item = q.pop()
    assert item == "I", "pop() should dequeue 'I' (the first item added)"
    assert len(q) == 2, "length should be 2"

    item = q.pop()
    assert item == "am", "pop() should dequeue 'am' (the second item added)"
    assert len(q) == 1, "length should be 1"

    q.push("one")
    print("Add another item:", q)
    assert len(q) == 2, "length should be 2"

    item = q.pop()
    assert item == "the", "pop() should dequeue 'the'"
    assert len(q) == 1, "length should be 1"

    print("Check the final list:", q)
