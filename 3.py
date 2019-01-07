import tkinter

# create main window
root = tkinter.Tk()

one = tkinter.Label(root, text="One", bg="red", fg="white")
one.pack()
two = tkinter.Label(root, text="Two", bg="green", fg="black")
two.pack(fill=tkinter.X)
three = tkinter.Label(root, text="Three", bg="blue", fg="white")
three.pack(side=tkinter.LEFT, fill=tkinter.Y)



# run window in loop
root.mainloop()