class hash_table:
    
    def __init__(self, max):
        """ Create a fixed size list based on the maxium number items """
        self.max = max
        self.lst = []
        for i in range(0, self.max):
            self.lst.append(None)
    
    
    def _hash(self, item, max):
        num = 0
        for i in range(len(item)-1):
            num = num + ord(item[i]) * i
        return num % max
    
    
    def get(self, item):
        """ get the item from the list """
        return self.lst[self._hash(item, self.max)]
    
    
    def set(self, item):
        """ add the item to the list """
        # add to the the list
        self.lst[self._hash(item, self.max)] = item
        
    
    def delete(self, item):
        """ void item """
        self.lst[self._hash(item, self.max)] = None
    
    
    def __str__(self):
        """ returns a string representation of the object using 'str(list)' (or 'print(list)') """
        return str(self.lst)
        
        

products = hash_table(26)
products.set("Ice cream")
products.set("XY")
products.set("YX")
products.set("Fries")
products.set("Burger")
products.set("XXXX")
print(products)


        
