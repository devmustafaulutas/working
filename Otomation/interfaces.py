
class İnterfaces():
    def main(self):
        print("""
------------------------------------------------
                İPEK PİŞMANİYE          
    1 ) Products Managment
    2 ) Accounting
    3 ) Managing
    4 ) Exit
------------------------------------------------""")
        
    def product_managment_interface(self):
            print("""
------------------------------------------------
                İPEK PİŞMANİYE          
    1 ) Show all products
    2 ) Add product
    3 ) Delete product
    4 ) Update product
    5 ) Exit
------------------------------------------------""")

    def categorys(self):
        print("""
------------------------------------------------
                İPEK PİŞMANİYE          
    1 ) Pismaniye
    2 ) Kestane Şekeri
    3 ) Çekme Helva
    4 ) Exit
------------------------------------------------""")
    def break_point(self):
         print("""    
------------------------------------------------
                İPEK PİŞMANİYE          
    1 ) Continue
    0 ) Exit
------------------------------------------------""")
    def accounting_interface(self):
        print("""    
------------------------------------------------
                İPEK PİŞMANİYE          
    1 ) Daily report
    2 ) Restock
    3 ) Daily Calculation
    4 ) Exit
------------------------------------------------""")

    def managing_interface(self):
        print("""    
------------------------------------------------
                İPEK PİŞMANİYE          
    1 ) Daily Accounting
    2 ) Workers
    3 ) Exit
------------------------------------------------""")
    def calculation_false(self,dailysale,cash,credit_card,expenses,discount,calc):
        print(f"""    
------------------------------------------------
                THE VALUES
    1 ) Daily Sales : {dailysale}
    2 ) Cash : {cash}
    3 ) Credit Card : {credit_card}
    4 ) Expenses : {expenses}
    5 ) Discount : {discount}
    6 ) Calculation : {calc} 
------------------------------------------------""")
    def daily_report_update_interface(self):
        print("""    
------------------------------------------------
                İPEK PİŞMANİYE          
    1 ) Daily Report Update
    0 ) Continue
------------------------------------------------""")
    def manage_workers(self):
        print("""    
------------------------------------------------
                İPEK PİŞMANİYE          
    1 ) Show Workers
    2 ) Add Worker
    3 ) Delete Worker
    4 ) Update Worker
    5 ) Exit
------------------------------------------------""")
    