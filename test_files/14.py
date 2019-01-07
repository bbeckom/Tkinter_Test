import tkinter


root = tkinter.Tk()

photo = tkinter.PhotoImage(file="mypic.png")
label = tkinter.Label(root, image=photo)

label.pack()

root.mainloop()
