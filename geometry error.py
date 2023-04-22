#bad geometry error
from tkinter import *
root=Tk()

root.title("geometry error")
try:
    root.geometry("100")
except:
    print("bad geometry error")
root.mainloop()