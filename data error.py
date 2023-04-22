#data type error & message box
from tkinter import *
from tkinter import messagebox
root=Tk()

root.title("data error")
root.geometry("400x400")

a=Entry(root)
a.place(relx=0.5,rely=0.2,anchor=CENTER)
b=Label(root)
b.place(relx=0.5,rely=0.9,anchor=CENTER)


def add():
    num=5
    num2=a.get()
    try:
        sum1=num2+num
        b["text"]=str(sum1)
    except:
        messagebox.showwarning("error","two different data types")
        

btn=Button(root,text="sum",command=add)
btn.place(relx=0.5,rely=0.7,anchor=CENTER)
    
root.mainloop() 