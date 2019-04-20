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
        return num % max
    
    
    def __getitem__(self, key):
        """ get the key from the list """
        
        h = self._hash(key, self.max)
        
        return self.lst[h]
    
    
    def __setitem__(self, key, value):
        """ add the key to the list """
        
        h = self._hash(key, self.max)
        
        self.lst[h] = value
        
    
    def __delitem__(self, key):
        """ void key """
        
        h = self._hash(key, self.max)
        
        self.lst[h] = None
    
    
    def __str__(self):
        """
        returns a string representation of the
        object using 'str(list)' (or 'print(list)')
        """
        
        return str(self.lst)
        
# dictionary

products = {
    "AA123":"burgar",
    "AZ456":"ice cream"
    }

print(products)

# add

products["B789"] = "fries"
products["ZZ"] = "veggie"
print(products)

# update
products["AA123"] = "burger"
print(products)

# delete
del products["B789"]
print(products)

# custom hash table
print("MY CUSTOM HASH TABLE")

my_hash_table = hash_table(256)
print(my_hash_table)

# add
my_hash_table["AA123"] = "burgar"
my_hash_table["AZ456"] = "ice cream"
my_hash_table["B789"] = "fries"
my_hash_table["ZZ"] = "veggie"
print(my_hash_table)

# update
print(my_hash_table["AA123"])
my_hash_table["AA123"] = "burger"
print(my_hash_table["AA123"])

# delete
del my_hash_table["B789"]
print(my_hash_table)


        


        
