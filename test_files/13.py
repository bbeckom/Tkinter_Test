import tkinter


root = tkinter.Tk()

canvas = tkinter.Canvas(root, width=200, height=100)
canvas.pack()

blackLine = canvas.create_line(0, 0, 200, 100)
redLine = canvas.create_line(200, 0, 0, 100, fill="red")
greenBox = canvas.create_rectangle(75, 25, 125, 50, fill="blue")

canvas.delete(redLine)
# to delete all... canvas.delete(tkinter.ALL)

root.mainloop()
