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
['NFe33200733240768000191550010000029001492586314', 'newbie'],
['NFe35191142274696002561550010040410901297528776', 'newbie'],
['NFe41210810640539000401550010000017581310588369', 'newbie']
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

to_be_checked = []
def not_checked_invoices():
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
