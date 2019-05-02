""" A mock static array as python only has lists """
class StaticArray:
    def __init__(self, fixed_size):
        # create a static array
        self._lst = []
        for i in range(fixed_size):
            self._lst.append(None)
        # the number of items with a non-Null value
        self._virtual_length = 0

    def remove(self, index):
        """ set the item at index position to None """
        self._lst[index] = None
        # Decrement the length
        self._virtual_length = self._virtual_length - 1

    def put(self, index, item):
        """ set the item at index postion """
        self._lst[index] = item
        # increment the length
        self._virtual_length = self._virtual_length + 1
        
    def get(self, index):
        return self._lst[index]
        
    def __str__(self):
        """ Implement special method to return string: A string representation of the list"""
        return str(self._lst)
    
    def __len__(self):
        """ Implement special method to return the length of the list: Number of item with non-NULL values """
        return self._virtual_length