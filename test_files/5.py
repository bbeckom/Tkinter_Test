import tkinter

# create main window
root = tkinter.Tk()

def printName():
    print("Ben")

button_1 = tkinter.Button(root, text="Print my name", command=printName)
button_1.pack()

# run window in loop
root.mainloop()