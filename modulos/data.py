from multiprocessing import connection
import sqlite3
from contextlib import closing

def invoice_check():
    connection = sqlite3.connect("invoice_check.db")
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE invoice_check (
      id integer primary key autoincrement,
      invoice_id text,
      checking text      
    );
    """)
    connection.close()

invoices_examples = [
['NFe31200806347409006953550190002601621173891452', 'newbie'],
['NFe31200806347409006953550310003371541174045999', 'newbie'],
['NFe35191142274696002561550010040410901297528776', 'newbie']
]

def insert_examples():
    connection = sqlite3.connect("invoice_check.db")
    cursor = connection.cursor()
    cursor.executemany("""
    INSERT INTO invoice_check (invoice_id, checking) 
    VALUES (?,?)
    """, invoices_examples)
    connection.commit()
    connection.close()

def all_invoices():
    connection = sqlite3.connect("invoice_check.db")
    cursor = connection.cursor()
    cursor.execute("""
    SELECT * FROM invoice_check;
    """)
    for i in cursor.fetchall():
        print(i)
    connection.close()


def not_checked_invoices():
    to_be_checked = []
    with sqlite3.connect("invoice_check.db") as connection:
        with closing(connection.cursor()) as cursor:
            cursor.execute("select * from invoice_check where checking = 'newbie'")
            while True:
                query_result = cursor.fetchone()
                if query_result is None:
                    break
                iterable_result = [query_result[1], query_result[2]]
                to_be_checked.append(iterable_result)
    return to_be_checked

def sales_table():
    connection = sqlite3.connect("sold_products.db")
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE sold_products (
      id integer primary key autoincrement,
      product text,
      price text,
      id_NFe
    );
    """)
    connection.close()

sold_products_examples = [
    ['MUNHEQUEIRA TENNIS WB L', '17.99', 'NFe35191142274696002561550010040410901297528776'],
    ['CAMISETA ID LINEAGE TEE', '47.99', 'NFe35191142274696002561550010040410901297528776'],
    ['SHORTS 3S KNIT W', '42.00', 'NFe35191142274696002561550010040410901297528776'],
    ['CAMISETA BB PRINT TEE 1', '59.99', 'NFe35191142274696002561550010040410901297528776'], 
    ['CAMISETA M GRFX LNR T 2', '42.00', 'NFe35191142274696002561550010040410901297528776'],
    ['CAMISETA M V M', '47.99', 'NFe35191142274696002561550010040410901297528776'],
    ['BERMU MP OXER PERF TRAINING 5G 204', '21.24', 'NFe31200806347409006953550190002601621173891452'], 
    ['BERMU MP OXER PERF TRAINING 62 204', '21.24', 'NFe31200806347409006953550190002601621173891452'],
    ['FUNCIONA OXER PERF 32 MOLA AC 02 000', '299.99', 'NFe31200806347409006953550310003371541174045999'], 
    ['FUNCIONA ACTE PERF T12 3CM 02 221', '89.99', 'NFe31200806347409006953550310003371541174045999']
]

def insert_sales_examples():
    connection = sqlite3.connect("sold_products.db")
    cursor = connection.cursor()
    cursor.executemany("""
    INSERT INTO sold_products (product, price, id_NFe) 
    VALUES (?,?,?)
    """, sold_products_examples)
    connection.commit()
    connection.close()

def delete_record():
    
    with sqlite3.connect("sold_products.db") as connection:
        with closing(connection.cursor()) as cursor:
            cursor.execute("""delete from sold_products
                where product = "BERMU MP OXER PERF TRAINING 62 204" """)
            print("Registros apagados: ", cursor.rowcount)
            if cursor.rowcount == 1:
                connection.commit()
                print("Alterações gravadas.")
            else:
                connection.rollback()
                print("Alterações abortadas")

def all_sales_examples():
    connection = sqlite3.connect("sold_products.db")
    cursor = connection.cursor()
    cursor.execute("""
    SELECT * FROM sold_products;
    """)
    for i in cursor.fetchall():
        print(i)
    connection.close()