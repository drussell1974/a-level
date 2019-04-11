class hash_table:
    
    def __init__(self, max_code):
        """ Create a fixed size list """
        self.length = 0
        self.lst = []
        for i in range(0, self.getHashCode(max_code) + 1):
            self.lst.append(None)
            
    
    def __getitem__(self, key):
        """ get the item from the list using the hash """
        return self.lst[self.getHashCode(key)]
    
    
    def __setitem__(self, key, value):
        """ add the item to the list """
        # update into the list
        self.lst[self.getHashCode(key)] = value
        self.length = self.length + 1
        
    
    def __delitem__(self, key):
        """ void item """
        self.lst[self.getHashCode(key)] = None
        self.length = self.length - 1
    
    
    def __len__(self):
        return self.length
    
    
    def __str__(self):
        return str(self.lst)
        
        
    def getHashCode(self, key):
        hash = 0
        for ch in key:
            hash = hash + ord(str(ch))
        return hash - 65
    

products = hash_table("ZZZZZ")

products["A"] = "ice cream"
print(products.getHashCode("A"))
print(products.getHashCode("ZZZZZ"))
products["ZZZZZ"] = "burger"
print(products)
print(len(products))

        
