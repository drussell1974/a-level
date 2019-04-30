import io
from classes import Product

PRODUCTDATA_FILENAME = "ProductData.txt"

def get_product(id):
    """ Get specific product from the ProductData file """
    
    f = open(PRODUCTDATA_FILENAME, "r")
    
    prod = Product() # default
    
    for row in f.readlines():
        cols = row.split(",") # seperate line
        if int(cols[0]) == id:
            ''' create new procuct instance and assign values in construct '''
            prod = Product(id = cols[0], name = cols[1], price = cols[2], quanity_in_stock = cols[3])
                        
    return prod


def get_all_products():
    """ Get all products from the ProductData file """
    
    ''' open file for reading '''
    f = open(PRODUCTDATA_FILENAME, "r")
    
    productList = []
    
    for row in f.readlines():
        cols = row.split(",") # seperate line
        ''' create new procuct instance and assign values in construct '''
        prod = Product(id = cols[0], name = cols[1], price = cols[2], quanity_in_stock = cols[3])
        ''' add to product to list '''
        productList.append(prod)
        
    return productList


def add_product(prod):
    productList = get_all_products()
    productList.append(prod)
    
    ''' open ProductData file for writing '''
    f = open(PRODUCTDATA_FILENAME, "a")
    for item in productList:
        # write values as strings to text file comma seperated with each product on a new line
        f.write("%s,%s,%s,%s\n" % (item.id, item.name, item.price, item.quanity_in_stock))
    f.close()
