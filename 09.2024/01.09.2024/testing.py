from model import Muhasebe
from tabulate import tabulate

def print_table():

    data = Muhasebe.sayim()


    headers = ['ID','İSİM','FİYAT','ADET','KOD']


    print(tabulate(data,headers,tablefmt="grid"))



print_table()