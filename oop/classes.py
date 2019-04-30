class Base:
    def __init__(self, id, name):
        self.id = int(id)
        self.name = str(name)
        self.errors = []
       
    def has_errors(self):
        return len(self.errors) > 0
    
    def get_errors(self):
        return self.errors
    

class Product:
    def __init__(self, id = 0, name = "", price = 0.0, quanity_in_stock = 0):
        self.super().__init__(id, name)
        self.name = str(name)
        print(price)
        self.price = float(price)
        self.quanity_in_stock = int(quanity_in_stock)
    
        
class ProductType:
    def __init__(self, id, name):
        self.super().__init__(id, name)
