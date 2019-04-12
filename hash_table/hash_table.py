class hash_table:
    
    def __init__(self, sizeOfList):
        """ Create a fixed size list based on the maxium number items """
        self.length = 0
        self.lst = []
        for i in range(0, sizeOfList):
            self.lst.append(None)
            
    
    def get(self, item):
        """ get the item from the list """
        return self.lst[ord(item[0])]
    
    
    def set(self, item):
        """ add the item to the list """
        # add to the the list
        self.lst[ord(item[0])] = item
        self.length = self.length + 1
        
    
    def delete(self, item):
        """ void item """
        self.lst[ord(item[0])] = None
        self.length = self.length - 1
    
    
    def __len__(self):
        """ returns the number of items in the list when using 'len(list)' """
        return self.length
    
    
    def __str__(self):
        """ returns a string representation of the object using 'str(list)' (or 'print(list)') """
        return str(self.lst)
        
        

products = hash_table(65 + 26)
products.set("Ice cream")
products.set("Fries")
products.set("Burger")
print(products)


        
