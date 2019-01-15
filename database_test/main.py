# Simple program to mess around with a SQLite DB

import tkinter
import database_test.db_actions as db


class MyApp(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        # set title
        self.title("Database Test Program")
        # remove maximize button and set window size
        self.resizable(0, 0)
        self.geometry("600x480")
        # new main window area
        self.mainwindow = tkinter.Text(self, bg="white", fg="black")
        self.mainwindow.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
        # set default main window text... using state to enable and disable the text box
        self.mainwindow.insert(tkinter.INSERT, "Simple SQLite DB program to mess around with.\n"
                                               "Choose a button below.")
        # create frame sections for pack layout
        self.topFrame = tkinter.Frame(self)
        self.topFrame.pack(fill=tkinter.X)
        self.midFrame = tkinter.Frame(self)
        self.midFrame.pack(fill=tkinter.X)
        self.bottomFrame = tkinter.Frame(self)
        self.bottomFrame.pack(side=tkinter.BOTTOM, fill=tkinter.X)
        # create entry fields and set values
        self.entries = self.entry_fields()
        self.entry1 = self.entries[0]
        self.entry1Text = self.entries[1]
        self.entry2 = self.entries[2]
        self.entry2Text = self.entries[3]
        self.stored_entry_1_text = "init text"
        self.stored_entry_2_text = "init text"
        # create buttons
        self.buttons_create()
        # create menu
        self.menu_create()
        # create status bar
        self.status_bar = self.status_create()
        # print init text to console
        print("init text")

    def list_name_button(self, val=''):
        entry1 = self.entry1.get()
        print(entry1)
        name = entry1
        # run db list_individual command with what was put into entry1
        result = db.list_individual(name)
        result = result.fetchall()
        # reconfigure status bar to display entry1 text
        self.status_bar.config(text=result)
        # delete text entry area
        self.delete_main_window()
        # add new content to text area
        self.mainwindow.insert(tkinter.INSERT, str(result))
        # store current entry
        self.stored_entry_1_text = str(result)

    def list_all_button(self, val=''):
        entry1 = self.entry1.get()
        print(entry1)
        # run list all db function
        result = db.list_names()
        result = result.fetchall()
        # reconfigure status bar to display entry text
        self.status_bar.config(text=result)
        # delete text entry area
        self.delete_main_window()
        # add new content to text area
        self.mainwindow.insert(tkinter.INSERT, str(result))

    def sql_query_button(self, val=''):
        entry2 = self.entry2.get()
        print(entry2)
        # run db query function
        result = db.sql_query(entry2)
        result = result.fetchall()
        # reconfigure status bar to display entry text
        self.status_bar.config(text=result)
        # delete text entry area
        self.delete_main_window()
        # add new content to text are
        self.mainwindow.insert(tkinter.INSERT, str(result))
        # clear out entry field and store current entry
        self.stored_entry_2_text = str(result)

    def add_button(self, val=''):
        entry1 = self.entry1.get()
        print(entry1)
        # run db add function
        result = db.add_name(entry1)
        result = result.fetchall()
        # reconfigure status bar to display entry text
        self.status_bar.config(text=result)
        # delete text entry area
        self.delete_main_window()
        # add new content to text are
        self.mainwindow.insert(tkinter.INSERT, str(result))
        # clear out entry field and store current entry
        self.stored_entry_1_text = str(result)

    def delete_button(self, val=''):
        entry1 = self.entry1.get()
        print(entry1)
        # run db delete command
        result = db.remove_name(entry1)
        result = result.fetchall()
        # reconfigure status bar to display entry text
        self.status_bar.config(text=result)
        # delete text entry area
        self.delete_main_window()
        # add new content to text are
        self.mainwindow.insert(tkinter.INSERT, str(result))
        # clear out entry field and store current entry
        self.stored_entry_1_text = str(result)

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
        sub_menu.add_command(label="Enable text field", command=self.enable_main_window)
        sub_menu.add_command(label="Disable text field", command=self.disable_main_window)
        sub_menu.add_separator()
        sub_menu.add_command(label="Exit", command=self.quit)

    def status_create(self):
        # status bar at bottom of app
        status = tkinter.Label(self.bottomFrame, text='init text', bd=1, relief=tkinter.SUNKEN, anchor=tkinter.W,
                               wraplength=600, height=1)
        status.pack(side=tkinter.BOTTOM, fill=tkinter.X)

        return status

    def buttons_create(self):
        # entry 1 buttons
        lind_button = tkinter.Button(self.topFrame, text="List Ind", command=self.list_name_button)
        lind_button.pack(side=tkinter.RIGHT)

        lall_button = tkinter.Button(self.topFrame, text="List All", command=self.list_all_button)
        lall_button.pack(side=tkinter.RIGHT)

        del_button = tkinter.Button(self.topFrame, text="Del name", command=self.delete_button)
        del_button.pack(side=tkinter.RIGHT)

        add_button = tkinter.Button(self.topFrame, text="Add name", command=self.add_button)
        add_button.pack(side=tkinter.RIGHT)
        # entry 2 buttons
        sql_button = tkinter.Button(self.midFrame, text="Run query", command=self.sql_query_button)
        sql_button.pack(side=tkinter.RIGHT)

    def entry_fields(self):
        # entry field 1 and label
        entry1_text = tkinter.StringVar()
        entry1 = tkinter.Entry(self.topFrame, textvariable=entry1_text)
        entry1_text.set('')
        entry1_label = tkinter.Label(self.topFrame, text="NAME_table", anchor=tkinter.E, width=10)
        entry1_label.pack(side=tkinter.LEFT)
        entry1.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)
        # entry field 2 and label
        entry2_text = tkinter.StringVar()
        entry2 = tkinter.Entry(self.midFrame, textvariable=entry2_text)
        entry2_text.set('')
        entry2_label = tkinter.Label(self.midFrame, text="SQL", anchor=tkinter.E, width=10)
        entry2_label.pack(side=tkinter.LEFT)
        entry2.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)

        return entry1, entry1_text, entry2, entry2_text


# start app
app = MyApp()
app.mainloop()
