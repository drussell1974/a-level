class hash_table:
    
    def __init__(self, sizeOfList):
        """ Create a fixed size list """
        
        # initial values
        self._startat = 0
        self._endat = 0
        self._freepointer = 0
        self.lst = []
        
        # Add empty items to the list
        for i in range(0, sizeOfList):
            self.lst.append(None)
            
    