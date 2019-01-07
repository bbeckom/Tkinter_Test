import tkinter

def SimplePrint():
    print("nothing")

class MyApp(tkinter.Tk):
    def __init__(self):

        tkinter.Tk.__init__(self)
        self.entry = tkinter.Entry(self)
        self.button = tkinter.Button(self, text="Get Input", command=self.on_button)
        self.button.pack()
        self.entry.pack()
        self.menucreate()

    def on_button(self):
        print(self.entry.get())

    def menucreate(self):
        self.mymenu = tkinter.Menu(self)
        self.config(menu=self.mymenu)

        self.subMenu = tkinter.Menu(self.mymenu, tearoff=0)
        self.mymenu.add_cascade(label="File", menu=self.subMenu)

        self.subMenu.add_command(label="Print text", command=SimplePrint)
        self.subMenu.add_separator()
        self.subMenu.add_command(label="Exit", command=self.quit)


app = MyApp()
app.mainloop()
