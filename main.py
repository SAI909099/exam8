import os
import psycopg2
from psycopg2 import sql

def get_db_connection():
    conn = psycopg2.connect(
        host='localhost',
        port='5432',
        user='postgres',
        password='1',
        dbname='books_db'
    )
    return conn

def create_table():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS book (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            price DECIMAL NOT NULL
        );
    """)
    conn.commit()
    cur.close()
    conn.close()

def add_book(name, price):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO book (name, price) VALUES (%s, %s)", (name, price))
    conn.commit()
    cur.close()
    conn.close()
    print("Kitob muvaffaqiyatli qo'shildi.")

def view_books():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, price FROM book")
    books = cur.fetchall()
    cur.close()
    conn.close()
    if books:
        print("{:<5} {:<30} {:<10}".format("ID", "Nomi", "Narxi"))
        for book in books:
            print("{:<5} {:<30} {:<10}".format(book[0], book[1], book[2]))
    else:
        print("Hech qanday kitob topilmadi.")

def main_menu():
    while True:
        print("\nMenu:")
        print("1. Kitob qo'shish")
        print("2. Kitoblarni ko'rish")
        print("3. Chiqish")

        choice = input("Tanlovni kiriting (1/2/3): ")

        if choice == '1':
            name = input("Kitob nomini kiriting: ")
            price_input = input("Kitob narxini kiriting: ")
            try:
                price = float(price_input)
                add_book(name, price)
            except ValueError:
                print("Iltimos, to'g'ri narx kiriting (raqam).")
        elif choice == '2':
            view_books()
        elif choice == '3':
            print("Dasturdan chiqildi.")
            break
        else:
            print("Noto'g'ri tanlov. Iltimos, qayta urinib ko'ring.")

if __name__ == "__main__":
    create_table()
    main_menu()

