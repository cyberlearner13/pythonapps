import psycopg2

def create_table():
    conn = psycopg2.connect("dbname='db1' user='postgres' password='postcoder108' host='localhost' port='5432'")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER,price REAL)")
    conn.commit()
    conn.close()

#create_table()

def insert_into_table(item,quantity,price):
    conn = psycopg2.connect("dbname='db1' user='postgres' password='postcoder108' host='localhost' port='5432'")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO store VALUES(%s,%s,%s)",(item,quantity,price) )
    conn.commit()
    conn.close()


#insert_into_table('doormat',5,27)
#insert_into_table('Water glass',10,7)


def delete(item):
    conn = psycopg2.connect("dbname='db1' user='postgres' password='postcoder108' host='localhost' port='5432'")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM store WHERE item=%s",(item,))
    conn.commit()
    conn.close()

#delete('Water glass')

def update(quantity,price,item):
    conn = psycopg2.connect("dbname='db1' user='postgres' password='postcoder108' host='localhost' port='5432'")
    cursor = conn.cursor()
    cursor.execute("UPDATE store SET quantity=%s,price=%s WHERE item=%s",(quantity,price,item))
    conn.commit()
    conn.close()

update(11,65.6,'doormat')
def view():
    conn = psycopg2.connect("dbname='db1' user='postgres' password='postcoder108' host='localhost' port='5432'")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM store")
    rows = cursor.fetchall()
    conn.close()
    return rows

print(view())



