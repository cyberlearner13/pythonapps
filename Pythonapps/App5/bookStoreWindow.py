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
import backend 


def view_command():
    list1.delete("1.0",END)
    for row in backend.view():
        list1.insert(END,row)

def search_command():
    list1.delete("1.0",END)
    for row in backend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        list1.insert(END,row)

def add_command():
    backend.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
        

def update_command():
    print()
def delete_command():
    print()
def close_command():
    print()

window = Tk()

label_t = Label(window,text="Title")
label_t.grid(row=0,column=0)

label_a = Label(window,text="Author")
label_a.grid(row=0,column=2)

label_y = Label(window,text="Year")
label_y.grid(row=1,column=0)

label_i = Label(window,text="ISBN")
label_i.grid(row=1,column=2)

title_text = StringVar()
title=Entry(window)
title.grid(row=0,column=1,textvariable=title_text)

author_text = StringVar()
author=Entry(window)
author.grid(row=0,column=3,textvariable=author_text)

year_text = StringVar()
year=Entry(window)
year.grid(row=1,column=1,textvariable=year_text)

isbn_text = StringVar()
isbn=Entry(window)
isbn.grid(row=1,column=3,textvariable=isbn_text)


list1=Text(window,height=8,width=45)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)


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

close=Button(window,text="Close",width=12,command=close_command)
close.grid(row=8,column=3)

window.mainloop()
