import mysql.connector

class DataBase:
    @staticmethod
    def connect_db():
        con = mysql.connector.connect(
            host='localhost',
            user='root',
            password='12345678',
            database='ipek_pismaniye'
        )
        return con
    
    def __init__(self):
        self.con = DataBase.connect_db()
        self.cursor = self.con.cursor()
        
    def cur(self):
        return self.cursor

    def create_tables(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS pismaniyeler (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            quantity INT,
            price DECIMAL(10, 2),
            code INT
        )""")

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS kestane_sekerleri (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            quantity INT,
            price DECIMAL(10, 2),
            code INT
        )""")       

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS cekme_helvalar (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            quantity INT,
            price DECIMAL(10, 2),
            code INT
        )""")
        
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS restock (
            id INT AUTO_INCREMENT PRIMARY KEY,
            date DATE NOT NULL,
            restock_bill DECIMAL(10, 2),
            category VARCHAR(100),
            code INT,
            quantity INT
        )""")
        
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS daily_reports (
            id INT AUTO_INCREMENT PRIMARY KEY,
            date DATE NOT NULL,
            daily_sales DECIMAL(10, 2) NOT NULL,
            cash DECIMAL(10, 2) NOT NULL,
            credit_card DECIMAL(10, 2),
            expenses DECIMAL(10, 2),
            discounts DECIMAL(10, 2),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
        )""")
        
        self.cursor.close()
        self.con.close()
