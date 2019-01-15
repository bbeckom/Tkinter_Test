# Simple program that will echo what is put into input field

import tkinter
import pyperclip
import database_test.db_actions as db


# simple function to test commands for menu selections quickly
def simple_print(val=''):
    # call the app variable that is created upon execution and change statusbar and main text to static string
    app.status_bar.config(text="Text printed")
    # set main window text then disable again
    app.delete_main_window()
    app.mainwindow.insert(tkinter.INSERT, "Text printed")
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
        # remove maximize button and set window size
        self.resizable(0, 0)
        self.geometry("600x480")
        # new main window area
        self.mainwindow = tkinter.Text(self, bg="white", fg="black")
        self.mainwindow.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
        # set default main window text... using state to enable and disable the text box
        self.mainwindow.insert(tkinter.INSERT, "INIT TEXT")
        # create frame sections for pack layout
        self.topFrame = tkinter.Frame(self)
        self.topFrame.pack(fill=tkinter.X)
        self.bottomFrame = tkinter.Frame(self)
        self.bottomFrame.pack(side=tkinter.BOTTOM, fill=tkinter.X)
        # create entry fields and set values
        self.entries = self.entry_fields()
        self.entry1 = self.entries[0]
        self.entry1Text = self.entries[1]
        self.stored_entry_1_text = "init text"
        # create buttons
        self.buttons_create()
        # create menu
        self.menu_create()
        # create status bar
        self.status_bar = self.status_create()
        # bind enter key to push getButton
        self.bind('<Return>', self.add_button)
        # print init text to console
        print("init text")

    def on_button(self, event=''):
        print(self.entry1.get())
        # reconfigure status bar to display entry text
        self.status_bar.config(text=self.entry1.get())
        # delete text entry area
        self.delete_main_window()
        # add new content to text are
        self.mainwindow.insert(tkinter.INSERT, self.entry1.get())
        # clear out entry field and store current entry
        self.stored_entry_1_text = str(self.entry1Text.get())
        self.entry1Text.set('')

    def list_name_button(self, val=''):
        print(self.entry1.get())
        name = self.entry1.get()
        # reconfigure status bar to display entry text
        result = db.list_individual(name)
        result = result.fetchall()
        self.status_bar.config(text=result)
        # delete text entry area
        self.delete_main_window()
        # add new content to text are
        self.mainwindow.insert(tkinter.INSERT, str(result))
        # clear out entry field and store current entry
        self.stored_entry_1_text = str(result)
        self.entry1Text.set('')

    def add_button(self, val=''):
        print(self.entry1.get())
        name = self.entry1.get()
        # reconfigure status bar to display entry text
        result = db.add_name(name)
        result = result.fetchall()
        self.status_bar.config(text=result)
        # delete text entry area
        self.delete_main_window()
        # add new content to text are
        self.mainwindow.insert(tkinter.INSERT, str(result))
        # clear out entry field and store current entry
        self.stored_entry_1_text = str(result)
        self.entry1Text.set('')


    def enable_main_window(self):
        window = self.mainwindow
        window.config(state=tkinter.NORMAL)

    def disable_main_window(self):
        window = self.mainwindow
        window.config(state=tkinter.DISABLED)

    def delete_main_window(self):
        window = self.mainwindow
        window.delete(1.0, tkinter.END)

    def menu_create(self):
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
        sub_menu.add_command(label="Enable text field", command=self.enable_main_window)
        sub_menu.add_command(label="Disable text field", command=self.disable_main_window)
        sub_menu.add_separator()
        sub_menu.add_command(label="Exit", command=self.quit)

    def status_create(self):
        # create sunken label at bottomFrame... wrap length is set ot window size and height is the lines of text
        status = tkinter.Label(self.bottomFrame, text='init text', bd=1, relief=tkinter.SUNKEN, anchor=tkinter.W,
                               wraplength=600, height=1)
        status.pack(side=tkinter.BOTTOM, fill=tkinter.X)

        return status

    def buttons_create(self):
        # button for entry field
        add_button = tkinter.Button(self.topFrame, text="Add name", command=self.add_button)
        add_button.pack(side=tkinter.RIGHT)

        lind_button = tkinter.Button(self.topFrame, text="List Ind", command=self.list_name_button)
        lind_button.pack(side=tkinter.RIGHT)

    def entry_fields(self):
        # entry field 1
        entry1_text = tkinter.StringVar()
        entry1 = tkinter.Entry(self.topFrame, textvariable=entry1_text)
        entry1_text.set('')
        entry1.pack(side=tkinter.LEFT, fill=tkinter.X, expand=True)

        return entry1, entry1_text


# start app
app = MyApp()
app.mainloop()
