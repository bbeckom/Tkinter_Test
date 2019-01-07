import tkinter

# create main window
root = tkinter.Tk()

def printName(event):
    print(event)

button_1 = tkinter.Button(root, text="Print my name")
button_1.bind('<Button-1>', printName)
button_1.pack()

# run window in loop
root.mainloop()