import tkinter


class ButtonProg:

    def __init__(self, master):
        frame = tkinter.Frame(master)
        frame.pack()

        self.printButton = tkinter.Button(frame, text="Print Message", command=self.printMessage)
        self.printButton.pack(side=tkinter.LEFT)

        self.quitButton = tkinter.Button(frame, text="Quit", command=frame.quit)
        self.quitButton.pack(side=tkinter.RIGHT)

    def printMessage(self):
        print("you clicked the button")



root = tkinter.Tk()
b = ButtonProg(root)
root.mainloop()