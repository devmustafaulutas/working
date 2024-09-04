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

        if category_selection ==1:category = 'pismaniyeler'
        elif category_selection==2:category = 'kestane_sekerleri'
        elif category_selection==3:category = 'cekme_helvalar'
        else:raise ValueError

        self.query.products(category)
        
        while True:
            try:
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
            except ValueError as err : print(err)
            except Exception as e: print(f"An error occurred: {e}")


    def del_products(self):

        self.interfaces.categorys()
        category_selection = int(input("Selection: "))

        if category_selection ==1:category = 'pismaniyeler'
        elif category_selection==2:category = 'kestane_sekerleri'
        elif category_selection==3:category = 'cekme_helvalar'
        else:raise ValueError

        self.query.products(category)

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

        if category_selection ==1:category = 'pismaniyeler'
        elif category_selection==2:category = 'kestane_sekerleri'
        elif category_selection==3:category = 'cekme_helvalar'
        else:raise ValueError

        self.query.products(category)

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
            date = datetime.today().date()
            category_selection = int(input("Selection: "))

            if category_selection ==1:restock_category = 'pismaniyeler'
            elif category_selection==2:restock_category = 'kestane_sekerleri'
            elif category_selection==3:restock_category = 'cekme_helvalar'
            elif category_selection ==4:break
            else:raise ValueError

            restock_bill = int(input("Restock bill: "))

            while True:
                restock_product_code = int(input("Product code: "))
                restock_product_quantity = int(input("Product quantity: "))
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
        try:
            date = datetime.today().date()
            daily_sales = int(input("Daily sales amount: "))
            cash = int(input('Cash in the safe: '))
            credit_card = int(input('Credit card amount on the Z report: '))
            expenses = int(input("Daily expenses: "))
            discounts = int(input("Daily discounts: "))

            self.query.daily_reports(date,daily_sales,cash,credit_card,expenses,discounts)
            print("Daily report saved!")
        except ValueError as err : print(err)
        except Exception as e: print(f"An error occurred: {e}")

    def calculation(self):
        date = datetime.today().date()
        report_data = self.query.daily_report_check(date)
        
        data = []
        data.extend(report_data)
        tuple_data = data[0]
        dailysale,cash,credit_card,expenses,discount = [item for item in tuple_data]
        diffrence = tuple_data[0]-tuple_data[1]-tuple_data[2]-tuple_data[3]-tuple_data[4]

        if diffrence == 0: print("The calculation is correct !")
        elif abs(diffrence) <= 100: print(f"The calculation is nearly correct , the diffrence is :{diffrence}")
        else : 
            self.interfaces.calculation_false(dailysale,cash,credit_card,expenses,discount,diffrence)
            while True:
                self.interfaces.daily_report_update_interface()
                selection = int(input("Selection : "))
                if selection ==1: self.update_daily_report()
                elif selection ==0:break
                else: raise ValueError

    def update_daily_report(self):
        try:
            date = datetime.today().date()
            daily_sale = int(input("Daily sales amount: "))
            cash = int(input('Cash in the safe: '))
            credit_card = int(input('Credit card amount on the Z report: '))
            expenses = int(input("Daily expenses: "))
            discounts = int(input("Daily discounts: "))
            
            self.query.daily_report_update(date, daily_sale, cash, credit_card, expenses, discounts)

            print("The daily report has been updated successfully!")
        except ValueError as err:
            print(f"Invalid input: {err}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def add_worker(self,name, salary, hire_date):
        try:
            name = input("Worker name: ")
            salary = int(input("Daily salary: "))
            hire_date = input("Hire date: ")

            self.query.add_worker(name,salary,hire_date)

            print("Worker saved successfully!")
        except ValueError as err:print(f"Invalid input: {err}")
        except Exception as e : print(f"An error occured: {e}")

    def update_worker(self,name, salary, hire_date):
        try:
            worker_id = int(input("Worker id: "))
            name = input("Worker name: ")
            salary = int(input("Daily salary: "))
            hire_date = input("Hire date: ")

            self.query.update_worker(name,salary,hire_date,worker_id)

            print("Worker saved successfully!")
        except ValueError as err:print(f"Invalid input: {err}")
        except Exception as e : print(f"An error occured: {e}")
    
    def del_worker(self):
        try:
            self.query.show_workers()
            worker_id = int(input("Worker id for deleting: "))

            self.query.del_worker(worker_id)               
            print("Worker deleted successfully!")

        except ValueError as err:print(f"Invalid input: {err}")
        except Exception as e : print(f"An error occured: {e}")
                

