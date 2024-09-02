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

        if selection_2 ==1:
            function.all_products()
        elif selection_2 ==2:
            function.add_products()
        elif selection_2 ==3:
            function.del_products()
        elif selection_2 ==4:
        elif selection_2 ==5:
            print("#")
    elif selection ==2:
        print("#")
    elif selection ==3:
        print("#")
    
    elif selection ==4:
        print("Have a great day!")
