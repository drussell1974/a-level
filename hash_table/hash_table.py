class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
    
    
    def __hash__(self):
        return getHashCode()
        
        
    def getHashCode(self):
        hash = 0
        for ch in self.key:
            hash = hash + ord(str(ch))
        return hash
    

class hash_table:
    
    def __init__(self, sizeOfList):
        """ Create a fixed size list based on the maxium number items """
        self.length = 0
        self.lst = []
        for i in range(0, sizeOfList):
            self.lst.append(None)
            
    
    def get(self, node):
        """ get the item from the list using 'obj = list[key]' """
        return self.lst[self.getHashCode(key)]
    
    
    def set(self, key, node):
        """ add the item to the list using 'list[key] = obj' """
        # update into the list
        self.lst[self.getHashCode(key)] = value
        self.length = self.length + 1
        
    
    def delete(self, node):
        """ void item using 'del list[key]' """
        self.lst[self.getHashCode(key)] = None
        self.length = self.length - 1
    
    
    def __len__(self):
        """ returns the number of items in the list when using 'len(list)' """
        return self.length
    
    
    def __str__(self):
        """ returns a string representation of the object using 'str(list)' """
        return str(self.lst)
        
        

    

products = hash_table(465)
products.set("A", "ice cream")
products.set("AZZZZ", "fries")
products.set("ZZZZZ", "burger")
print(len(products))
print(products)


        
