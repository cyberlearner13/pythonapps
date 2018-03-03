"""
A program that stores 
Title,Author,
Year,ISBN

User can:

View all records
Search an entry
Add entry
Update entry
Delete
Close

"""

from tkinter import *
from backend import Database

db = Database("books.db")

def get_selected_row(event):
    global selected_tuple
    try:
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)
        title.delete(0,END)
        title.insert(END,selected_tuple[1])
        author.delete(0,END)
        author.insert(END,selected_tuple[2])
        year.delete(0,END)
        year.insert(END,selected_tuple[3])
        isbn.delete(0,END)
        isbn.insert(END,selected_tuple[4])
    except IndexError:
        pass

def view_command():
    list1.delete(0,END)
    for row in db.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in db.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        list1.insert(END,row)

def add_command():
    db.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    list1.delete(0,END)
    list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))    

def update_command():
    db.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
def delete_command():
    db.delete(selected_tuple[0])


window = Tk()

window.wm_title("Book Store")

label_t = Label(window,text="Title")
label_t.grid(row=0,column=0)

label_a = Label(window,text="Author")
label_a.grid(row=0,column=2)

label_y = Label(window,text="Year")
label_y.grid(row=1,column=0)

label_i = Label(window,text="ISBN")
label_i.grid(row=1,column=2)

title_text = StringVar()
title=Entry(window,textvariable=title_text)
title.grid(row=0,column=1)

author_text = StringVar()
author=Entry(window,textvariable=author_text)
author.grid(row=0,column=3)

year_text = StringVar()
year=Entry(window,textvariable=year_text)
year.grid(row=1,column=1)

isbn_text = StringVar()
isbn=Entry(window,textvariable=isbn_text)
isbn.grid(row=1,column=3)


list1=Listbox(window,height=8,width=45)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

view_all=Button(window,text="View All",width=12,command=view_command)
view_all.grid(row=3,column=3)

search=Button(window,text="Search Entry",width=12,command=search_command)
search.grid(row=4,column=3)

add=Button(window,text="Add Entry",width=12,command=add_command)
add.grid(row=5,column=3)

update=Button(window,text="Update",width=12,command=update_command)
update.grid(row=6,column=3)

delete=Button(window,text="Delete",width=12,command=delete_command)
delete.grid(row=7,column=3)

close=Button(window,text="Close",width=12,command=window.destroy)
close.grid(row=8,column=3)

window.mainloop()
