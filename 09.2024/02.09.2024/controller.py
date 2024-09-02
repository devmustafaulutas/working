from model import Tables,Querys
from interfaces import İnterfaces

class Functions:
    def __init__(self):
        self.table = Tables()
        self.query = Querys()
        self.interfaces = İnterfaces()
        
    def all_products(self):
        self.table.all_products()
    
    def add_products(self):
        self.interfaces.categorys()
        category_selection = int(input("Selection: "))
        if category_selection ==1:
            category = 'pismaniyeler'
        elif category_selection==2:
            category = 'kestane_sekerleri'
        elif category_selection==3:
            category = 'cekme_helvalar'
        else:
            raise ValueError
        while True:
            self.interfaces.break_point()
            new_product_name = input("New product name: ")
            new_product_piece = int(input("New product piece: "))
            new_product_price = int(input("New product price: "))
            break_point = int(input("Selection: "))
            if break_point ==1:
                continue
            elif break_point == 0:
                break
        self.query.add_product(category,new_product_name,new_product_piece,new_product_price)

    def del_products(self):
        self.interfaces.categorys()
        category_selection = int(input("Selection: "))
        if category_selection ==1:
            category = 'pismaniyeler'
        elif category_selection==2:
            category = 'kestane_sekerleri'
        elif category_selection==3:
            category = 'cekme_helvalar'
        else:
            raise ValueError
        while True:
            self.interfaces.break_point()
            id_selection = int(input("Selection: "))
            self.query.del_product(category,id_selection)
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
        elif category_selection==2:
            category = 'kestane_sekerleri'
        elif category_selection==3:
            category = 'cekme_helvalar'
        else:
            raise ValueError
        while True:
            self.interfaces.break_point()
            new_product_name = input("New product name: ")
            new_product_piece = int(input("New product piece: "))
            new_product_price = int(input("New product price: "))
            self.query.update_product(category,new_product_name,new_product_piece,new_product_price)
            break_point = int(input("Selection: "))
            if break_point ==1:
                continue
            elif break_point == 0:
                break