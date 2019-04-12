class hash_table:
    
    def __init__(self, sizeOfList):
        """ Create a fixed size list based on the maxium number items """
        self.length = 0
        self.lst = []
        for i in range(0, sizeOfList):
            self.lst.append(None)
            
    
    def __getitem__(self, key):
        """ get the item from the list using 'obj = list[key]' """
        h = self.getHashCode(key)
        # check the location using the hash
        for item in self.lst[h]:
            # find the matching key
            if item[0] == key:
                # return the value
                return item[1]
        # or return nothing
        return None

    
    def __setitem__(self, key, value):
        """ add the item to the hash table using 'list[key] = obj' """
        # create a hash which will be the index
        h = self.getHashCode(key)
        # create a key value pair
        kv = [key, value]
        
        # store the items in the hash table (handle collisions)
        if self.lst[h] == None:
            # if the location is empty start a new list
            self.lst[h] = []
            self.lst[h].append(kv)
        else:
            # check the location using the value
            for item in self.lst[h]:
                # check if the key exists
                if item[0] == key:
                    item[1] = value
                    return True
            # otherwise append a new value to avoid a collision
            self.lst[h].append(kv)
                
                
        self.length = self.length + 1
        
    
    def __delitem__(self, key):
        """ void item using 'del list[key]' """
        h = self.getHashCode(key)
        # check the location using the hash
        for item in self.lst[h]:
            # ensure the key matches
            if item[0] == key:
                item[1] = None
                self.length = self.length - 1
    
    
    def __len__(self):
        """ returns the number of items in the list when using 'len(list)' """
        return len(self.lst)
    
    
    def __str__(self):
        """ returns a string representation of the object using 'str(list)' """
        return str(self.lst)
        
        
    def getHashCode(self, key):
        hash = 0
        for ch in key:
            hash = hash + ord(str(ch))
        return hash
        

    
p = hash_table(1)
products = hash_table(181)
products["AA"] = "burgar"  # add the first item
products["AZ"] = "ice cream"  # add a second item
products["ZA"] = "fries" # add a collision
products["AA"] = "burger" # update the first item
products["ZZ"] = "veggie" # add a last item
print(products["AZ"]) # show the first item in the collision
print(products["ZA"]) # show the second item in the collision
print(products["AA"]) # show the updated value
print(products)
        
