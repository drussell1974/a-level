class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
        
    def __eq__(self, other):
        """ Allow comparison of items """
        if self.value == other.value:
            return True
        
    def __str__(self):
        return str(self.value)
        
    
class linked_list:
    
    def __init__(self, sizeOfList):
        """ Create a fixed size list """
        
        # initial values
        self._startat = 0
        self._endat = 0
        self._freepointer = 0
        self.lst = []
        
        # Add empty items to the list
        for i in range(0, sizeOfList):
            new_node = Node()
            self.lst.append(new_node)
            
    
    def __getitem__(self, key):
        """ Dictionary """
        return self.lst[key]
    
    
    def append(self, value):
        # create new node with pointer
        nd = Node(value=value, next=0)
        
        # insert into next available space
        self.lst[self._freepointer] = nd
        
        # point the last item at the new item
        self.lst[self._endat].next = self._freepointer
        
        # store the index of the last item
        self._endat = self._freepointer
   
        self._updatePointer()
        
        
    def _updatePointer(self):
        """ update pointer """
        for item in self.lst:
            if item.next == None:
                self._freepointer = self.lst.index(item)
        else:
            self._freepointer = -1
         
        
    
    def delete(self, ptr):
        # update the pointer of the previous item
        for item in self.lst:
            if item.next == ptr:
                # the index of the item pointer that will be updated
                pptr = self.lst.index(item)
                # get the pointer from the item to be deleted
                currP = self.lst[ptr].next
                # the previous item now points to the next item
                self.lst[pptr].next = currP
                # void item to be deleted
        # the item deleted is the next free space
        self._freepointer = ptr
        
    
    
llist = linked_list(4)
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.append("E")

for item in llist:
    print(item)
    print(item.next)

        