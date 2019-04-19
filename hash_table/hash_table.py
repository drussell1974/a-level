class hash_table:
    
    def __init__(self, max):
        """ Create a fixed size list based on the maxium number keys """
        self.max = max
        self.lst = []
        for i in range(0, self.max):
            self.lst.append(None)
    
    
    def _hash(self, key, max):
        num = 0
        for i in range(len(key)-1):
            num = num + ord(key[i]) * i
        print(num % max)
        return num % max
    
    
    def __getitem__(self, key):
        """ get the key from the list """
        return self.lst[self._hash(key, self.max)]
    
    
    def __setitem__(self, key, value):
        """ add the key to the list """
        # add to the the list
        self.lst[self._hash(key, self.max)] = value
        
    
    def __delitem__(self, key):
        """ void key """
        self.lst[self._hash(key, self.max)] = None
    
    
    def __str__(self):
        """ returns a string representation of the object using 'str(list)' (or 'print(list)') """
        return str(self.lst)
        
        

products = hash_table(256)
products["AA123"] = "burgar"  # add the first item
products["AZ123"] = "ice cream"  # add a second item
products["ZA2"] = "fries" # add a collision
products["AA123"] = "burger" # update the first item
products["ZZ"] = "veggie" # add a last item
print(products["AZ"]) # show the first item in the collision
print(products["ZA"]) # show the second item in the collision
print(products["AB"]) # show the updated value
print(products)


        
