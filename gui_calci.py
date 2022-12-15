from tkinter import *


"for window creation"
root = Tk()

'text field'
output = Entry(root , width = 50 , borderwidth = 5 )
output.grid(row=0 , column=0 , columnspan=3 , padx=5 , pady= 3)

"functions used further defined first its mah way bitch"
def show(number):
    current = output.get()
    output.delete(0,END)
    output.insert(0,current + str(number))    
    

def plus():
    cur = output.get()
    global f_num
    global oper
    oper = "add"
    f_num = int(cur)
    output.delete(0,END)

def minus():
    cur = output.get()
    global f_num
    global oper
    oper = 'minus'
    f_num = int(cur)
    output.delete(0,END)

def multiply():
    cur = output.get()
    global f_num
    global oper
    oper = 'mul'
    f_num = int(cur)
    output.delete(0,END)


def divide():
    cur = output.get()
    global f_num
    global oper
    oper = 'div'
    f_num = int(cur)
    output.delete(0,END)

def mod():
    cur = output.get()
    global f_num
    global oper
    oper = 'mod'
    f_num = int(cur)
    output.delete(0,END)

def equals():
    nxt_num = output.get()
    output.delete(0,END)
    if oper == 'add':    
        output.insert(0,(f_num + int(nxt_num)))
    if oper == 'minus':
        output.insert(0,f_num - int(nxt_num))
    if oper == 'mul':
        output.insert(0,f_num * int(nxt_num))
    if oper == 'div':
        output.insert(0,f_num / int(nxt_num))
    if oper == 'mod':
        output.insert(0,f_num % int(nxt_num))

def clear():
    output.delete(0,END)

'creating all the buttons first bcz i want to'
button_1 = Button(root ,text='1' , padx= 40 , pady= 20 ,command=lambda : show(1))
button_2 = Button(root ,text='2' , padx= 40 , pady= 20 ,command=lambda : show(2))
button_3 = Button(root ,text='3' , padx= 40 , pady= 20 ,command=lambda : show(3))

button_4 = Button(root ,text='4' , padx= 40 , pady= 20 ,command=lambda : show(4))
button_5 = Button(root ,text='5' , padx= 40 , pady= 20 ,command=lambda : show(5))
button_6 = Button(root ,text='6' , padx= 40 , pady= 20 ,command=lambda : show(6))

button_7 = Button(root ,text='7' , padx= 40 , pady= 20 ,command=lambda : show(7))
button_8 = Button(root ,text='8' , padx= 40 , pady= 20 ,command=lambda : show(8))
button_9 = Button(root ,text='9' , padx= 40 , pady= 20 ,command=lambda : show(9))

button_0 = Button(root ,text='0' , padx= 40 , pady= 20 ,command=lambda : show(0))

button_add = Button(root ,text='+' , padx=39 , pady=20 , command= plus )
button_multiply = Button(root ,text='*' , padx=40 , pady=20 , command= multiply )
button_divide = Button(root ,text='/' , padx=40 , pady=20 , command= divide )
button_minus = Button(root ,text='-' , padx=40 , pady=20 , command= minus )
button_mod = Button(root ,text='%' , padx=38 , pady=20 , command= mod )

button_equal = Button(root , text="=" ,padx=39 , pady= 20 , command=equals)

button_clr = Button(root ,text='clear' , padx=101, pady=20 , command=clear )

'griding all saperately for cleaner code or say to increase lines (hehe bitch)'
button_1.grid(row = 3 , column = 2 )
button_2.grid(row = 3 , column = 1 )
button_3.grid(row = 3 , column = 0 )

button_4.grid(row = 2 , column = 2 )
button_5.grid(row = 2 , column = 1 )
button_6.grid(row = 2 , column = 0 )

button_7.grid(row = 1 , column = 2 )
button_8.grid(row = 1 , column = 1 )
button_9.grid(row = 1 , column = 0 )

button_0.grid(row = 4, column = 0)

button_add.grid(row=4,column=1)
button_minus.grid(row=4,column=2)
button_multiply.grid(row=5,column=1)
button_divide.grid(row=5,column=2)
button_equal.grid(row=5,column=0)
button_mod.grid(row=6,column=0)
button_clr.grid(row=6,column=1,columnspan=2) 

'mainloop to keep it running till we press close in gui buttons'
ok = root.mainloop()


' finished bitched now go get some hoes u fking nerds'