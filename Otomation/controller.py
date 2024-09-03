from model import Querys
from interfaces import İnterfaces
from datetime import datetime

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
            new_product_code = int(input("New product code: "))
            self.query.add_product(category,new_product_name,new_product_quantity,new_product_price,new_product_code)

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
            new_code = int(input("New code: "))
            self.query.update_product(category,product_id,new_name,new_quantity,new_price,new_code)

            self.interfaces.break_point()
            break_point = int(input("Selection: "))
            if break_point == 1:
                continue
            elif break_point ==0:
                break
            else: 
                raise ValueError        
    
    def restock(self):
        while True:
            self.interfaces.categorys()
            date = datetime.strptime(date , "%d-%m-%y").date()
            category_selection = int(input("Selection: "))
            if category_selection ==1:restock_category = 'pismaniyeler'
            elif category_selection==2:restock_category = 'kestane_sekerleri'
            elif category_selection==3:restock_category = 'cekme_helvalar'
            else:raise ValueError
            restock_bill = int(input("Restock bill: "))
            while True:
                restock_product_code = int(input("Product code: "))
                restock_product_quantity = int(input("Product quantity"))
                self.query.restock(date,restock_bill,restock_category,restock_product_code,restock_product_quantity)
                self.interfaces.break_point()
                break_point = int(input("Selection: "))
                if break_point == 1:
                    continue
                elif break_point ==0:
                    break
                else:raise ValueError
            break

    def daily_report(self):
        while True:
            date = datetime.strptime(date , "%d-%m-%y").date()
            daily_sales = int(input("Daily sales amount: "))
            cash = int(input('Cash in the safe: '))
            credit_card = int(input('Credit card amount on the z report'))
            expenses = int(input("Daily expenses: "))
            discounts = int(input("Daily discounts: "))
            self.query.daily_reports(date,daily_sales,cash,credit_card,expenses,discounts)
            print("Have a great day!")
            break
    