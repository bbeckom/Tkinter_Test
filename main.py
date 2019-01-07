# Simple program that will echo what is put into input field

import tkinter


# simple function to test commands for menu selections quickly
def SimplePrint(val=''):
    # call the app variable that is created upon execution and change statusbar and canvas text to static string
    app.statusbar.config(text="Text printed")
    app.logoCanvas.itemconfigure(app.logoText, text="Text printed")
    print("Text printed")


class MyApp(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        # create frame sections for pack layout
        self.topFrame = tkinter.Frame(self)
        self.topFrame.pack(fill=tkinter.X)
        self.bottomFrame = tkinter.Frame(self)
        self.bottomFrame.pack(side=tkinter.BOTTOM, fill=tkinter.X)
        # put in canvas
        self.myLogo = self.myCanvas()
        self.logoCanvas = self.myLogo[0]
        self.logoText = self.myLogo[1]
        # entry field
        self.entrytext = tkinter.StringVar()
        self.entry = tkinter.Entry(self.topFrame, textvariable=self.entrytext)
        self.entrytext.set("")
        # button for entry field
        self.getButton = tkinter.Button(self.topFrame, text="Get Input", command=self.on_button)
        # pack button and entry field
        self.getButton.pack(side=tkinter.RIGHT)
        self.entry.pack(side=tkinter.LEFT, fill=tkinter.X, expand=True)
        # create menu
        self.mainMenu = self.menucreate()
        # create status bar
        self.statusbar = self.statuscreate()
        # bind enter key to push getButton
        self.bind('<Return>', self.on_button)
        # print init text to console
        print("init text")

    def on_button(self, event=''):
        print(self.entry.get())
        # reconfigure statusbar to display entry text
        self.statusbar.config(text=self.entry.get())
        # reconfigure logo text object, I returned the canvas and text objects created in myCanvas
        logoCanvas = self.logoCanvas
        logoText = self.logoText
        logoCanvas.itemconfigure(logoText, text=self.entry.get())
        # clear out entry field
        self.entrytext.set("")



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

    def myCanvas(self):
        # create logo space
        self.canvas = tkinter.Canvas(self.topFrame, width=600, height=480)
        self.canvas.pack()
        # just a bunch of random objects drawn
        self.canvas.create_rectangle(0, 0, 600, 480, fill="brown")
        self.canvas.create_line(0, 0, 600, 480, width=2)
        self.canvas.create_line(600, 0, 0, 480, width=2)
        self.canvas.create_line(600, 240, 0, 240, width=2)
        self.canvas.create_line(300, 0, 300, 480, width=2)
        # create initial text
        self.text_1 = self.canvas.create_text(300, 240, text="init text", font=("Purisa",22), fill="white")
        return self.canvas, self.text_1


# start app
app = MyApp()
app.mainloop()
