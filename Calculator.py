from tkinter import *
def button_click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0,current+str(number))
def button_clear():
    e.delete(0,END)
def button_add():
   first_number= e.get()
   global math
   math="add"
   global first
   first= int(first_number)
   e.delete(0,END)
def button_equals():
    second_number=e.get()
    e.delete(0,END)
    second=int(second_number)
    if math=="add":
     e.insert(0,first+second)
    elif math=="subtract":
        e.insert(0,first-second)
    elif math=="multply":
        e.insert(0,first*second)
    elif math=="divide":
        e.insert(0,first/second)

def button_subtract():
    first_number = e.get()
    global math
    math = "subtract"
    global first
    first = int(first_number)
    e.delete(0, END)
def button_multiply():
    first_number = e.get()
    global math
    math = "multply"
    global first
    first = int(first_number)
    e.delete(0, END)
def button_divide():
    first_number = e.get()
    global math
    math = "divide"
    global first
    first = int(first_number)
    e.delete(0, END)

root = Tk()
root.title("Calculator")


e=Entry(root,width=100,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
button_1=Button(root,text="1",padx=40,pady=20,command=lambda:button_click(1))
button_2=Button(root,text="2",padx=40,pady=20,command=lambda:button_click(2))
button_3=Button(root,text="3",padx=40,pady=20,command=lambda:button_click(3))
button_4=Button(root,text="4",padx=40,pady=20,command=lambda:button_click(4))
button_5=Button(root,text="5",padx=40,pady=20,command=lambda:button_click(5))
button_6=Button(root,text="6",padx=40,pady=20,command=lambda:button_click(6))
button_7=Button(root,text="7",padx=40,pady=20,command=lambda:button_click(7))
button_8=Button(root,text="8",padx=40,pady=20,command=lambda:button_click(8))
button_9=Button(root,text="9",padx=40,pady=20,command=lambda:button_click(9))
button_0=Button(root,text="0",padx=40,pady=20,command=lambda:button_click(0))
button_add=Button(root,text="+",padx=39,pady=20,command=button_add)
button_equal=Button(root,text="=",padx=39,pady=20,command=button_equals)
button_clear=Button(root,text="clear",padx=80,pady=20,command=button_clear)
button_subtract=Button(root,text="-",padx=39,pady=20,command=button_subtract)
button_multiply=Button(root,text="*",padx=39,pady=20,command=button_multiply)
button_division=Button(root,text="/",padx=39,pady=20,command=button_divide)

button_0.grid(row=4,column=0,columnspan=2)

button_1.grid(row=3,column=0,columnspan=2)
button_2.grid(row=3,column=1,columnspan=2)
button_3.grid(row=3,column=2,columnspan=2)

button_4.grid(row=2,column=0,columnspan=2)
button_5.grid(row=2,column=1,columnspan=2)
button_6.grid(row=2,column=2,columnspan=2)

button_7.grid(row=1,column=0,columnspan=2)
button_8.grid(row=1,column=1,columnspan=2)
button_9.grid(row=1,column=2,columnspan=2)

button_add.grid(row=5,column=0,columnspan=2)
button_equal.grid(row=5,column=1,columnspan=2)
button_clear.grid(row=6,column=1,columnspan=2)
button_subtract.grid(row=7,column=0,columnspan=2)
button_multiply.grid(row=7,column=1,columnspan=2)
button_division.grid(row=7,column=2,columnspan=2)
root.mainloop()