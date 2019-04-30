class Product:
    def __init__(self, id = 0, name = "", price = 0.0, quanity_in_stock = 0):
        self.id = int(id)
        self.name = str(name)
        print(price)
        self.price = float(price)
        self.quanity_in_stock = int(quanity_in_stock)
    
        
class ProductType:
    def __init__(self, id, name):
        self.id = int(id)
        self.name = name
