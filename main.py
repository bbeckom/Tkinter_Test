# Simple program that will echo what is put into input field

import tkinter
import pyperclip


# simple function to test commands for menu selections quickly
def simple_print(val=''):
    # call the app variable that is created upon execution and change statusbar and canvas text to static string
    app.status_bar.config(text="Text printed")
    app.mainwindowCanvas.itemconfigure(app.mainwindowText, text="Text printed")
    print("Text printed")
    app.stored_entry_1_text = "Text printed"


# use downloaded pyperclip package to store to system clipboard
def simple_copy():
    pyperclip.copy(app.stored_entry_1_text)


class MyApp(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        # set title
        self.title("Test Program")
        # remove maximize button
        self.resizable(0, 0)
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
        self.entries = self.entry_fields()
        self.entry1 = self.entries[0]
        self.entry1Text = self.entries[1]
        self.stored_entry_1_text = "init text"
        # create buttons
        self.buttons_create()
        # create menu
        self.menucreate()
        # create status bar
        self.status_bar = self.statuscreate()
        # bind enter key to push getButton
        self.bind('<Return>', self.on_button)
        # print init text to console
        print("init text")

    def on_button(self, event=''):
        print(self.entry1.get())
        # reconfigure status bar to display entry text
        self.status_bar.config(text=self.entry1.get())
        # reconfigure logo text object, I returned the canvas and text objects created in myCanvas
        main_window_canvas = self.mainwindowCanvas
        main_window_text = self.mainwindowText
        main_window_canvas.itemconfigure(main_window_text, text=self.entry1.get())
        # clear out entry field and store current entry
        self.stored_entry_1_text = str(self.entry1Text.get())
        self.entry1Text.set("")

    def menucreate(self):
        # create menu and set to app with self.config
        main_menu = tkinter.Menu(self)
        self.config(menu=main_menu)
        # File menu
        sub_menu = tkinter.Menu(main_menu, tearoff=0)
        main_menu.add_cascade(label="File", menu=sub_menu)
        # File submenu options
        sub_menu.add_command(label="Print text", command=simple_print)
        sub_menu.add_command(label="Copy current text", command=simple_copy)
        sub_menu.add_separator()
        sub_menu.add_command(label="Exit", command=self.quit)

    def statuscreate(self):
        # create sunken label at bottomFrame... wrap length is set ot window size and height is the lines of text
        status = tkinter.Label(self.bottomFrame, text='init text', bd=1, relief=tkinter.SUNKEN, anchor=tkinter.W,
                               wraplength=600, height=1)
        status.pack(fill=tkinter.X)

        return status

    def myCanvas(self):
        # create logo space
        canvas = tkinter.Canvas(self.topFrame, width=600, height=480)
        canvas.pack()
        # just a bunch of random objects drawn
        canvas.create_rectangle(0, 0, 600, 480, fill="brown")
        canvas.create_line(0, 0, 600, 480, width=2, fill="white")
        canvas.create_line(600, 0, 0, 480, width=2, fill="red")
        canvas.create_line(600, 240, 0, 240, width=2, fill="blue")
        canvas.create_line(300, 0, 300, 480, width=2, fill="yellow")
        # create initial text
        text_1 = canvas.create_text(300, 240, text="init text", font=("Purisa", 25, "bold"), fill="black",
                                    width=580)

        return canvas, text_1

    def buttons_create(self):
        # button for entry field
        get_button = tkinter.Button(self.topFrame, text="Get Input", command=self.on_button)
        get_button.pack(side=tkinter.RIGHT)

    def entry_fields(self):
        # entry field 1
        entry1_text = tkinter.StringVar()
        entry1 = tkinter.Entry(self.topFrame, textvariable=entry1_text)
        entry1_text.set("")
        entry1.pack(side=tkinter.LEFT, fill=tkinter.X, expand=True)

        return entry1, entry1_text


# start app
app = MyApp()
app.mainloop()
