import tkinter


# simple function to test commands for now
def SimplePrint():
    print("nothing")


class MyApp(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.entry = tkinter.Entry(self)
        self.getButton = tkinter.Button(self, text="Get Input", command=self.on_button)
        self.getButton.pack()
        self.entry.pack()
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
        self.status = tkinter.Label(self, text='init', bd=1, relief=tkinter.SUNKEN, anchor=tkinter.W)
        self.status.pack(side=tkinter.BOTTOM, fill=tkinter.X)
        return self.status


app = MyApp()
app.mainloop()
