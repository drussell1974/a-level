class Base:
    def __init__(self, id):
        self.id = int(id)
        clear_errors()
        
    def clear_errors():
        self.errors = []
       
    def add_error(self, message):
        self.errors.append(message)
        
    def has_errors(self):
        return len(self.errors) > 0
    
    def get_errors(self):
        return self.errors
    

class Product(Base):
    def __init__(self, id = 0, name = "", price = 0.0, quanity_in_stock = 0):
        self.super().__init__(id)
        set_name(name)
        set_price(price)
        set_quanity_in_stock(quanity_in_stock)
    
    def set_name(name):
        if len(name) > 50:
            add_error("Name cannot exceed 50 characters")
        else:    
            self.name = str(name)
            
    def set_price(price):
        if float(price) < 0:
            add_error("Price must be a positive number")
        else:
            self.price = float(price)
                        
    def set_quanity_in_stock(quanity_in_stock):
        if int(quanity_in_stock) < 0:
            add_error("Quanity in stock must be a positive number")
        else:
            self.price = int(quanity_in_stock)

            
class ProductType(Base):
    def __init__(self, id, name):
        self.super().__init__(id, name)
        self.name = str(name)
        
    def set_name(name):
        if len(name) > 20:
            add_error("Name cannot exceed 20 characters")
        else:    
            self.name = str(name)
