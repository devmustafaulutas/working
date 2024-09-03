import mysql.connector
from database import DataBase

class Querys:
    def __init__(self):
        self.con = DataBase.connect_db()
        self.cursor = self.con.cursor()

    def close_connection(self):
        self.cursor.close()
        self.con.close()

    def all_products(self):
        query = """
        SELECT id, name, quantity, price, code FROM pismaniyeler
        UNION
        SELECT id, name, quantity, price, code FROM kestane_sekerleri
        UNION
        SELECT id, name, quantity, price, code FROM cekme_helvalar;
        """
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        print(data)
    
    def products(self, category):
        query = f"SELECT * FROM {category}"
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        print(data)

    def add_product(self, category, name, quantity, price, code):
        query = f"INSERT INTO {category} (name, quantity, price) VALUES (%s, %s, %s, %s)"
        values = (name, quantity, price, code)
        try:
            self.cursor.execute(query, values)
            self.con.commit()
            print("Product added successfully!")
        except mysql.connector.Error as error:
            print("Failed to add product: {}".format(error))
            self.con.rollback()
        finally:
            self.close_connection()

    def del_product(self, category, id):
        query = f"DELETE FROM {category} WHERE id = %s"
        try:
            self.cursor.execute(query, (id,))
            self.con.commit()
            print("Product deleted successfully!")
        except mysql.connector.Error as error:
            print("Failed to delete product: {}".format(error))
            self.con.rollback()
        finally:
            self.close_connection()

    def update_product(self, category, product_id, new_name, new_quantity, new_price, new_code):
        query = f"UPDATE {category} SET name = %s, quantity = %s, price = %s, code = %s WHERE id = %s"
        values = (new_name, new_quantity, new_price, new_code, product_id)
        try:
            self.cursor.execute(query, values)
            self.con.commit()
            print("Product updated successfully!")
        except mysql.connector.Error as error:
            print("Failed to update product: {}".format(error))
            self.con.rollback()
        finally:
            self.close_connection()

    def restock(self,date,restock_bill,category,code,quantity):
        query = "INSERT INTO restock SET date = %s, restock_bill = %s, category = %s, code = %s, quantity = %s"
        values = (date,restock_bill,category,code,quantity)
        try:
            self.cursor.execute(query,values)
            self.con.commit()
        except mysql.connector.Error as error:
            print(f"Failed to save restock: {error}")
        finally:
            self.con.close()

    def daily_reports(self,date,daily_sales,cash,credit_card,expenses,discounts):
        query = "INSERT INTO daily_reports SET date = %s, daily_sales = %s, cash =%s , credit_card = %s, expenses=%s, discounts =%s"
        values = (date,daily_sales,cash,credit_card,expenses,discounts)
        try:
            self.cursor.execute(query,values)
            self.con.commit()
        except mysql.connector.Error as error:
            print(f"Failed to save daily report: {error}")
        finally:
            self.con.close()
    