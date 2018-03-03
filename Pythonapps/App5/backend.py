import sqlite3

class Database:

    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.cur_obj = self.conn.cursor()
        self.cur_obj.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY, title TEXT, author TEXT,year INTEGER,isbn INTEGER)")
        self.conn.commit()

    def insert(self,title,author,year,isbn):
        conn = sqlite3.connect("books.db")
        cur_obj = conn.cursor()
        cur_obj.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(title,author,year,isbn))
        conn.commit()
        conn.close()

    def view(self):
        self.cur_obj.execute("SELECT * FROM book")
        rows = self.cur_obj.fetchall()
        return rows

    def update(self,id,title,author,year,isbn):
        self.cur_obj.execute("UPDATE book SET title=?,author=?,year=?,isbn=? WHERE id=? ",(title,author,year,isbn,id ))
        self.conn.commit()

    def search(self,title="",author="",year="",isbn=""):
        self.cur_obj.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
        rows = self.cur_obj.fetchall()
        return rows

    def delete(self,id):
        self.cur_obj.execute("DELETE FROM book WHERE id=?",(id,))
        self.conn.commit()
    
    def __del__(self):
        self.conn.close()

# insert("The deer","Ian Smith",2017,11293355843)
# insert("The ghost","Brian Sands",2012,10293355843)
# insert("The sweater","Liam Jones",2013,13293355843)
# insert("The horse","Jon Frost",2010,12293355843)

#print(search(author="Ian Smith"))
#print(view())


#delete(5)





