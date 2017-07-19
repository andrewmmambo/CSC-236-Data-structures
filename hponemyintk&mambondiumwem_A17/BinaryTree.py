from Tkinter import *

root = Tk()

photo1 = PhotoImage(file="1.gif")
photo2 = PhotoImage(file="2.gif")
photo3 = PhotoImage(file="3.gif")

w = Label(root, image=photo1).place(x=0, y=0, relwidth=0.25, relheight=0.4)
w.pack(fill=X)
w = Label(root, image=photo2).place(x=0, y=0, relwidth=0.25, relheight=0.4)
w.pack(fill=X)
w = Label(root, image=photo3).place(x=0, y=0, relwidth=0.25, relheight=0.4)
w.pack(fill=X)

mainloop()