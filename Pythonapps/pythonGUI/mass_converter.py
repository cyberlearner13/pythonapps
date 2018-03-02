from tkinter import *

window = Tk()

def convert_mass():
   mass_to_convert = float(mass_in_kg.get())
   mass_in_grams = mass_to_convert * 1000
   mass_in_pounds = mass_to_convert * 2.20462 
   mass_in_ounces = mass_to_convert * 35.274
   t1.insert(END,mass_in_grams)
   t2.insert(END,mass_in_pounds)
   t3.insert(END,mass_in_ounces)

label = Label(window,text="Kg",width=5)
label.grid(row=0,column=1)

mass_in_kg=StringVar()
e1=Entry(window,textvariable=mass_in_kg)
e1.grid(row=0,column=2)

b1=Button(window,text="Convert",command=convert_mass)
b1.grid(row=0,column=3)

t1=Text(window,height=1,width=20)
t1.grid(row=1,column=1)

t2=Text(window,height=1,width=20)
t2.grid(row=1,column=2)

t3=Text(window,height=1,width=20)
t3.grid(row=1,column=3)

window.mainloop()