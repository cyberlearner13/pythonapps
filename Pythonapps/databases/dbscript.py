import sqlite3

def create_table():
    conn = sqlite3.connect("lite.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER,price REAL)")
    conn.commit()
    conn.close()



def insert_into_table(item,quantity,price):
    conn = sqlite3.connect("lite.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO store VALUES(?,?,?)",(item,quantity,price))
    conn.commit()
    conn.close()



#insert_into_table('Water glass',10,7)


def delete(item):
    conn = sqlite3.connect("lite.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM store WHERE item=?",(item,))
    conn.commit()
    conn.close()

#delete('Water glass')

def update(quantity,price,item):
    conn = sqlite3.connect("lite.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE store SET quantity=?,price=? WHERE item=?",(quantity,price,item))
    conn.commit()
    conn.close()

update(11,6,'Wine Glass')
def view():
    conn = sqlite3.connect("lite.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM store")
    rows = cursor.fetchall()
    conn.close()
    return rows

print(view())



