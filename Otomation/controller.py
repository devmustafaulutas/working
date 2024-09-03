from model import Querys
from interfaces import İnterfaces

class Functions:

    def __init__(self):
        self.query = Querys()
        self.interfaces = İnterfaces()

    def show_products(self):
        self.query.all_products()

    def add_products(self):
        self.interfaces.categorys()
        category_selection = int(input("Selection: "))
        if category_selection ==1:
            category = 'pismaniyeler'
            self.query.products(category)
        elif category_selection==2:
            category = 'kestane_sekerleri'
            self.query.products(category)
        elif category_selection==3:
            category = 'cekme_helvalar'
            self.query.products(category)
        else:
            raise ValueError
        
        while True:
            new_product_name = input("New product name: ")
            new_product_quantity = int(input("New product quantity: "))
            new_product_price = int(input("New product price: "))
            self.query.add_product(category,new_product_name,new_product_quantity,new_product_price)

            self.interfaces.break_point()
            break_point = int(input("Selection: "))
            if break_point ==1:
                continue
            elif break_point == 0:
                break


    def del_products(self):
        self.interfaces.categorys()
        category_selection = int(input("Selection: "))
        if category_selection ==1:
            category = 'pismaniyeler'
            self.query.products(category)
        elif category_selection==2:
            category = 'kestane_sekerleri'
            self.query.products(category)
        elif category_selection==3:
            category = 'cekme_helvalar'
            self.query.products(category)
        else:
            raise ValueError
        
        while True:
            id_selection = int(input("Product id: "))
            self.query.del_product(category,id_selection)
            self.interfaces.break_point()
            break_point = int(input("Selection: "))
            if break_point ==1:
                continue
            elif break_point == 0:
                break

    def update_products(self):
        self.interfaces.categorys()
        category_selection = int(input("Selection: "))
        if category_selection ==1:
            category = 'pismaniyeler'
            self.query.products(category)
        elif category_selection==2:
            category = 'kestane_sekerleri'
            self.query.products(category)
        elif category_selection==3:
            category = 'cekme_helvalar'
            self.query.products(category)
        else:
            raise ValueError
        while True:
            product_id = int(input("The product id: "))
            new_name = input("New name: ")
            new_quantity = int(input("New quantity: "))
            new_price = int(input("New price: "))
            self.query.update_product(category,product_id,new_name,new_quantity,new_price)

            self.interfaces.break_point()
            break_point = int(input("Selection: "))
            if break_point == 1:
                continue
            elif break_point ==0:
                break
            else: 
                raise ValueError        
            