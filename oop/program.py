import datastore # import the whole module
from classes import Product # import specific class from module


def add_product():
    print("***********")
    print("ADD PRODUCT")
    product_id = int(input("Enter product id: "))
    product_name = input("Enter product name: ")
    product_price = float(input("Enter product price: "))
    product_qty = int(input("Enter number of items in stock: "))

    new_prod = Product(product_id, product_name, product_price, product_qty)

    datastore.add_product(new_prod)

def view_single_item():
    print("****************")
    print("VIEW SINGLE ITEM")
    product_id = int(input("Input product id: "))
    
    item = datastore.get_product(product_id)

    print(item.name, item.price, item.quanity_in_stock)
    
    
def view_all_items():
    print("**************")
    print("VIEW ALL ITEMS")
    stocklist = datastore.get_all_products()

    for item in stocklist:
        print(item.name, item.price, item.quanity_in_stock)
        

while True:
    print("*********")
    print("MAIN MENU")
    option = int(input("Enter option:\n1. Add product\n2. View Single Item\n3. View All Items\n"))
    if option == 1:
        add_product()
    elif option == 2:
        view_single_item()
    elif option == 3:
        view_all_items()
    else:
        print("Not a valid option! Please try again.")
