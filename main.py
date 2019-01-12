# Simple program that will echo what is put into input field

import tkinter
import pyperclip


# simple function to test commands for menu selections quickly
def SimplePrint(val=''):
    # call the app variable that is created upon execution and change statusbar and canvas text to static string
    app.statusbar.config(text="Text printed")
    app.mainwindowCanvas.itemconfigure(app.mainwindowText, text="Text printed")
    print("Text printed")
    app.storedendtry1Text = "Text printed"

#test
# use downloaded pyperclip package to store to system clipboard
def SimpleCopy():
    pyperclip.copy(app.storedendtry1Text)


class MyApp(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        # set title
        self.title("Test Program")
        # create frame sections for pack layout
        self.topFrame = tkinter.Frame(self)
        self.topFrame.pack(fill=tkinter.X)
        self.bottomFrame = tkinter.Frame(self)
        self.bottomFrame.pack(side=tkinter.BOTTOM, fill=tkinter.X)
        # put in canvas
        self.mainwindow = self.myCanvas()
        self.mainwindowCanvas = self.mainwindow[0]
        self.mainwindowText = self.mainwindow[1]
        # create entry fields and set values
        self.entries = self.entryFields()
        self.entry1 = self.entries[0]
        self.entry1Text = self.entries[1]
        self.storedendtry1Text = "init text"
        # create buttons
        self.buttons = self.buttonsCreate()
        # create menu
        self.mainMenu = self.menucreate()
        # create status bar
        self.statusbar = self.statuscreate()
        # bind enter key to push getButton
        self.bind('<Return>', self.on_button)
        # print init text to console
        print("init text")

    def on_button(self, event=''):
        print(self.entry1.get())
        # reconfigure statusbar to display entry text
        self.statusbar.config(text=self.entry1.get())
        # reconfigure logo text object, I returned the canvas and text objects created in myCanvas
        mainwindowCanvas = self.mainwindowCanvas
        mainwindowText = self.mainwindowText
        mainwindowCanvas.itemconfigure(mainwindowText, text=self.entry1.get())
        # clear out entry field and store current entry
        self.storedendtry1Text = str(self.entry1Text.get())
        self.entry1Text.set("")

    def menucreate(self):
        # create menu and set to app with self.config
        self.mymenu = tkinter.Menu(self)
        self.config(menu=self.mymenu)
        # File menu
        self.subMenu = tkinter.Menu(self.mymenu, tearoff=0)
        self.mymenu.add_cascade(label="File", menu=self.subMenu)
        # File submenu options
        self.subMenu.add_command(label="Print text", command=SimplePrint)
        self.subMenu.add_command(label="Copy current text", command=SimpleCopy)
        self.subMenu.add_separator()
        self.subMenu.add_command(label="Exit", command=self.quit)

    def statuscreate(self):
        # create sunken label at bottomFrame... wraplength is set ot window size and height is the lines of text
        self.status = tkinter.Label(self.bottomFrame, text='init text', bd=1, relief=tkinter.SUNKEN, anchor=tkinter.W,
                                    wraplength=600, height=1)
        self.status.pack(fill=tkinter.X)
        # return so we can update this object later
        return self.status

    def myCanvas(self):
        # create logo space
        self.canvas = tkinter.Canvas(self.topFrame, width=600, height=480)
        self.canvas.pack()
        # just a bunch of random objects drawn
        self.canvas.create_rectangle(0, 0, 600, 480, fill="brown")
        self.canvas.create_line(0, 0, 600, 480, width=2, fill="white")
        self.canvas.create_line(600, 0, 0, 480, width=2, fill="red")
        self.canvas.create_line(600, 240, 0, 240, width=2, fill="blue")
        self.canvas.create_line(300, 0, 300, 480, width=2, fill="yellow")
        # create initial text
        self.text_1 = self.canvas.create_text(300, 240, text="init text", font=("Purisa", 25, "bold"), fill="black",
                                              width=580)
        return self.canvas, self.text_1

    def buttonsCreate(self):
        # button for entry field
        self.getButton = tkinter.Button(self.topFrame, text="Get Input", command=self.on_button)
        self.getButton.pack(side=tkinter.RIGHT)

    def entryFields(self):
        # entry field
        self.entry1Text = tkinter.StringVar()
        self.entry1 = tkinter.Entry(self.topFrame, textvariable=self.entry1Text)
        self.entry1Text.set("")
        self.entry1.pack(side=tkinter.LEFT, fill=tkinter.X, expand=True)
        return self.entry1, self.entry1Text


# start app
app = MyApp()
app.mainloop()
