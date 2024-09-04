from interfaces import İnterfaces
from controller import Functions

interface = İnterfaces()
function = Functions()
while True:
    interface.main()
    selection = int(input("Selection: "))

    if selection ==1:

        interface.product_managment_interface()
        selection_2 = int(input("Selection: "))

        if selection_2 ==1:function.show_products()
        elif selection_2 ==2:function.add_products()
        elif selection_2 ==3:function.del_products()
        elif selection_2 ==4:function.update_products()
        elif selection_2 ==5:print("")
        else:raise ValueError
    
    elif selection ==2:

        interface.accounting_interface()
        selection_3 = int(input("Selection: "))

        if selection_3 ==1:function.daily_report()
        elif selection_3 ==2:function.restock()
        elif selection_3 ==3:function.calculation()

    elif selection ==3:
        
        interface.managing_interface()
        selection_4 = int(input("Selection: "))
        
    elif selection ==4:
        print("Have a great day!")
        break
