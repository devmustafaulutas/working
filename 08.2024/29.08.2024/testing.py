from model import sayim
from tabulate import tabulate

def print_table():

    data = sayim()


    headers = ['ID','İSİM','FİYAT','ADET','KOD']


    print(tabulate(data,headers,tablefmt="grid"))

print_table()