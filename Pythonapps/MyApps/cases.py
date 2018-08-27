from tkinter import *

window = Tk()

window.wm_title("Case Change")

label_t = Label(window,height=2,width=25,text="Enter variable name: ")
label_t.config(font=("Courier", 12))
label_t.grid(row=0,column=0)


label_y = Label(window,height=2,text="No special characters allowed!")
label_y.grid(row=1,column=1)



variable_name = StringVar()
title=Entry(window,width=25,textvariable=variable_name)
title.grid(row=0,column=1)

v = IntVar()
snake = Radiobutton(window,text="Snake Case",variable=v,value=1,width = 10)
snake.grid(row=2, column=0)

camel = Radiobutton(window,text="Camel Case",variable=v,value=2,width = 15)
camel.grid(row=2, column=1)

pascal = Radiobutton(window,text="Pascal Case",variable=v,value=3,width = 10)
pascal.grid(row=2, column=2)

extra= Label(window,text=" ",width=5)
extra.grid(row=2, column=3,columnspan=2)

window.mainloop()
