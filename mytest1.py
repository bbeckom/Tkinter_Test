import tkinter


# simple function to test commands for now
def SimplePrint():
    print("nothing")


class MyApp(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.topFrame = tkinter.Frame(self)
        self.topFrame.pack(fill=tkinter.X)
        self.bottomFrame = tkinter.Frame(self)
        self.bottomFrame.pack(side=tkinter.BOTTOM, fill=tkinter.X)
        self.entry = tkinter.Entry(self.topFrame)
        self.getButton = tkinter.Button(self.topFrame, text="Get Input", command=self.on_button)
        self.getButton.pack(side=tkinter.RIGHT)
        self.entry.pack(side=tkinter.LEFT, fill=tkinter.X, expand=True)
        self.menucreate()
        self.statusbar = self.statuscreate()

    def on_button(self):
        print(self.entry.get())
        self.statusbar.config(text=self.entry.get())

    def menucreate(self):
        self.mymenu = tkinter.Menu(self)
        self.config(menu=self.mymenu)

        # File menu
        self.subMenu = tkinter.Menu(self.mymenu, tearoff=0)
        self.mymenu.add_cascade(label="File", menu=self.subMenu)
        # File submenu options
        self.subMenu.add_command(label="Print text", command=SimplePrint)
        self.subMenu.add_separator()
        self.subMenu.add_command(label="Exit", command=self.quit)

    def statuscreate(self):
        self.status = tkinter.Label(self.bottomFrame, text='init', bd=1, relief=tkinter.SUNKEN, anchor=tkinter.W)
        self.status.pack(fill=tkinter.X)
        return self.status


app = MyApp()
app.mainloop()
