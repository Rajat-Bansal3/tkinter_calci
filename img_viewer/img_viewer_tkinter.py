from tkinter import * 
from PIL import Image,ImageTk

root = Tk()
root.title("Gallery")
root.iconbitmap("S:\gui\img\image-gallery.png")

img1 = ImageTk.PhotoImage(Image.open("1.jpg"))
img2 = ImageTk.PhotoImage(Image.open("2.webp"))
img3 = ImageTk.PhotoImage(Image.open("3.jpg"))
img4 = ImageTk.PhotoImage(Image.open("4.png"))
img5 = ImageTk.PhotoImage(Image.open("5.jpg"))
img6 = ImageTk.PhotoImage(Image.open("6.png"))

lst = [img1,img2,img3,img4,img5,img6]


i = 0



mylabel = Label(image=lst[i])
mylabel.grid(row = 0 , column = 0 , columnspan = 3)


def Next():
    global lst
    global i
    global mylabel
    i += 1 
    mylabel.destroy()
    mylabel = Label(image = lst[i])
    mylabel.grid(row = 0 , column = 0 , columnspan = 3)
    if i == len(lst) - 1:
        i = -1


def back():
    global lst
    global i
    global mylabel
    i -= 1
    mylabel.destroy()
    mylabel = Label(image = lst[i])
    mylabel.grid(row = 0 , column = 0 , columnspan = 3)
    if i == 0 :
        i = len(lst) -  1
    


back_but = Button(root,text="Back",command = lambda : back())
quit_but = Button(root,text="Quit",command = root.quit)
next_but = Button(root,text="Next",command = lambda : Next())

back_but.grid(row = 1,column = 0)
quit_but.grid(row = 1,column = 1)
next_but.grid(row = 1,column = 2)


root.mainloop()
