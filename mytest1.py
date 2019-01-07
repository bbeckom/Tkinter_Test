# Simple program that will echo what is put into input field

import tkinter


# simple function to test commands for now
def SimplePrint():
    print("nothing")


class MyApp(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        # create frame sections
        self.topFrame = tkinter.Frame(self)
        self.topFrame.pack(fill=tkinter.X)
        self.bottomFrame = tkinter.Frame(self)
        self.bottomFrame.pack(side=tkinter.BOTTOM, fill=tkinter.X)
        # entry field
        self.entry = tkinter.Entry(self.topFrame)
        # button for entry field
        self.getButton = tkinter.Button(self.topFrame, text="Get Input", command=self.on_button)
        # pack button and entry field
        self.getButton.pack(side=tkinter.RIGHT)
        self.entry.pack(side=tkinter.LEFT, fill=tkinter.X, expand=True)
        # create menu
        self.menucreate()
        # create status bar
        self.statusbar = self.statuscreate()

    def on_button(self):
        print(self.entry.get())
        # reconfigure statusbar to display entry text
        self.statusbar.config(text=self.entry.get())

    def menucreate(self):
        # create menu and set to app with self.config
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
        self.status = tkinter.Label(self.bottomFrame, text='init text', bd=1, relief=tkinter.SUNKEN, anchor=tkinter.W)
        self.status.pack(fill=tkinter.X)
        # return so we can update this object later
        return self.status


# start app
app = MyApp()
app.mainloop()
