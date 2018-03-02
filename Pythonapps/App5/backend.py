import sqlite3

def connect():
    conn = sqlite3.connect("books.db")
    cur_obj = conn.cursor()
    cur_obj.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY, title TEXT, author TEXT,year INTEGER,isbn INTEGER)")
    conn.commit()
    conn.close()

connect()

def insert(title,author,year,isbn):
    conn = sqlite3.connect("books.db")
    cur_obj = conn.cursor()
    cur_obj.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("books.db")
    cur_obj = conn.cursor()
    cur_obj.execute("SELECT * FROM book")
    rows = cur_obj.fetchall()
    conn.close()
    return rows

def update(id,title,author,year,isbn):
    conn = sqlite3.connect("books.db")
    cur_obj = conn.cursor()
    cur_obj.execute("UPDATE book SET title=?,author=?,year=?,isbn=? WHERE title=? OR author=? OR year=? OR isbn=? ",(title,author,year,isbn))
    conn.commit()
    conn.close()

def search(title="",author="",year="",isbn=""):
    conn = sqlite3.connect("books.db")
    cur_obj = conn.cursor()
    cur_obj.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
    rows = cur_obj.fetchall()
    conn.commit()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("books.db")
    cur_obj = conn.cursor()
    cur_obj.execute("DELETE FROM book WHERE id=?",(id,))
    conn.commit()
    conn.close()

# insert("The deer","Ian Smith",2017,11293355843)
# insert("The ghost","Brian Sands",2012,10293355843)
# insert("The sweater","Liam Jones",2013,13293355843)
# insert("The horse","Jon Frost",2010,12293355843)

print(search(author="Ian Smith"))
#print(view())

# delete(1)
# delete(2)
# delete(3)
# delete(4)
# delete(5)





