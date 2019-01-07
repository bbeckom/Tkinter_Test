import tkinter

# create main window
root = tkinter.Tk()

topFrame = tkinter.Frame(root)
topFrame.pack()
bottomFrame = tkinter.Frame(root)
bottomFrame.pack(side=tkinter.BOTTOM)

button1 = tkinter.Button(topFrame, text="Button 1", fg="red", bg="black")
button2 = tkinter.Button(topFrame, text="Button 2", fg="green", bg="black")
button3 = tkinter.Button(topFrame, text="Button 3", fg="purple", bg="black")
button4 = tkinter.Button(bottomFrame, text="Button 4", fg="blue", bg="black")


button1.pack(side=tkinter.LEFT)
button2.pack(side=tkinter.LEFT)
button3.pack(side=tkinter.LEFT)
button4.pack()

# run window in loop
root.mainloop()