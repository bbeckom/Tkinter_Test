import tkinter

# create main window
root = tkinter.Tk()

def leftClick(event):
    print("left")
    print(event)

def rightClick(event):
    print("right")
    print(event)

def middleClick(event):
    print("middle")
    print(event)


frame = tkinter.Frame(root, width=640, height=480)
frame.bind("<Button-1>", leftClick)
frame.bind("<Button-2>", middleClick)
frame.bind("<Button-3>", rightClick)

frame.pack()

# run window in loop
root.mainloop()