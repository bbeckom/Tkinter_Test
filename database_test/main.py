# Simple program to mess around with a SQLite DB

import tkinter
import database_test.db_actions as db
import database_test.help as hp
import pyperclip


def simple_copy():
    pyperclip.copy(app.mainwindow_text)


def refresh_mainwindow(*args):
    # delete
    window = app.mainwindow
    window.delete(1.0, tkinter.END)
    # insert
    app.mainwindow.insert(tkinter.INSERT, app.mainwindow_text)
    app.entry1Text.set('')
    app.entry2Text.set('')


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
        self.mainwindow_text = "Simple SQLite DB program to mess around with.\nChoose a button below."
        self.mainwindow.insert(tkinter.INSERT, self.mainwindow_text)
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
        self.entry1.bind("<Return>", self.add_button)
        self.entry1.bind("<Up>", self.entry1_scroll_up)
        self.entry1.bind("<Down>", self.entry1_scroll_down)
        self.entry1.bind("<FocusOut>", self.entry1_hist_reset)
        self.entry1Text = self.entries[1]
        self.entry2 = self.entries[2]
        self.entry2.bind("<Return>", self.sql_query_button)
        self.entry2.bind("<Up>", self.entry2_scroll_up)
        self.entry2.bind("<Down>", self.entry2_scroll_down)
        self.entry2.bind("<FocusOut>", self.entry2_hist_reset)
        self.entry2Text = self.entries[3]
        self.stored_entry_1_text = "init text"
        self.stored_entry_2_text = "init text"
        # list of entries and history country
        self.entry1_entries = []
        self.entry1_hist_count = 0
        self.entry2_entries = []
        self.entry2_hist_count = 0
        # create buttons
        self.buttons_create()
        # create menu
        self.menu_create()
        # create status bar
        self.status_bar = self.status_create()
        # print init text to console
        print("init text")

    def set_statusbar_text(self, input):
        status = self.status_bar
        input = str(input)
        if len(input) > 95:
            input = input[:95]
            input = str(input + "...")
        status.config(text=input)

    def list_name_button(self, *args):
        entry1 = self.entry1.get()
        print(entry1)
        name = entry1
        # run db list_individual command with what was put into entry1
        result = db.list_individual(name)
        result = result.fetchall()
        # reconfigure status bar to display entry1 text
        self.set_statusbar_text(result)
        # add new content to text area
        self.mainwindow_text = str(result)
        refresh_mainwindow()
        # store current entry
        self.entry1_store(name)

    def list_all_button(self, *args):
        # run list all db function
        result = db.list_names()
        result = result.fetchall()
        # reconfigure status bar to display entry text
        self.set_statusbar_text(result)
        # add new content to text area
        self.mainwindow_text = str(result)
        refresh_mainwindow()

    def entry1_store(self, text):
        self.stored_entry_1_text = str(text)
        try:
            self.entry1_entries.remove(self.stored_entry_1_text)
            self.entry1_entries.append(self.stored_entry_1_text)
        except ValueError:
            self.entry1_entries.append(self.stored_entry_1_text)

    def entry1_scroll_up(self, *args):
        # remove a value from the count so that it goes down every time button is pushed
        self.entry1_hist_count = self.entry1_hist_count-1
        # convert hist count to a positive number and see if it's greater than total entries, if so will restart count
        if len(self.entry1_entries) < -self.entry1_hist_count:
            self.entry1_hist_count = 0
            self.entry1Text.set('')
            return "break"  # have to do this because maxosx wants to insert a character when you press up or down
        self.entry1Text.set(self.entry1_entries[self.entry1_hist_count])
        # set cursor position to right of text
        self.entry1.icursor(len(self.entry1_entries[self.entry1_hist_count]))
        return "break"

    def entry1_scroll_down(self, *args):
        # add a value to the count so that it goes up every time button is pushed
        self.entry1_hist_count = self.entry1_hist_count+1
        # if entry1 count returns >= 0 then reset total back to the total entries -1
        if self.entry1_hist_count >= 0:
            total_entries = len(self.entry1_entries)
            self.entry1_hist_count = -total_entries-1
            self.entry1Text.set('')
            return "break"
        self.entry1Text.set(self.entry1_entries[self.entry1_hist_count])
        # set cursor position to right of text
        self.entry1.icursor(len(self.entry1_entries[self.entry1_hist_count]))
        return "break"

    def entry1_hist_reset(self, *args):
        self.entry1_hist_count = 0

    def entry2_store(self, text):
        self.stored_entry_2_text = str(text)
        try:
            self.entry2_entries.remove(self.stored_entry_2_text)
            self.entry2_entries.append(self.stored_entry_2_text)
        except ValueError:
            self.entry2_entries.append(self.stored_entry_2_text)

    def entry2_scroll_up(self, *args):
        # remove a value from the count so that it goes down every time button is pushed
        self.entry2_hist_count = self.entry2_hist_count-1
        # convert hist count to a positive number and see if it's greater than total entries, if so will restart count
        if len(self.entry2_entries) < -self.entry2_hist_count:
            self.entry2_hist_count = 0
            self.entry2Text.set('')
            return "break"  # have to do this because maxosx wants to insert a character when you press up or down
        self.entry2Text.set(self.entry2_entries[self.entry2_hist_count])
        # set cursor position to right of text
        self.entry2.icursor(len(self.entry2_entries[self.entry2_hist_count]))
        return "break"

    def entry2_scroll_down(self, *args):
        # add a value to the count so that it goes up every time button is pushed
        self.entry2_hist_count = self.entry2_hist_count+1
        # if entry2 count returns >= 0 then reset total back to the total entries -1
        if self.entry2_hist_count >= 0:
            total_entries = len(self.entry2_entries)
            self.entry2_hist_count = -total_entries-1
            self.entry2Text.set('')
            return "break"
        self.entry2Text.set(self.entry2_entries[self.entry2_hist_count])
        # set cursor position to right of text
        self.entry2.icursor(len(self.entry2_entries[self.entry2_hist_count]))
        return "break"

    def entry2_hist_reset(self, *args):
        self.entry2_hist_count = 0

    def sql_query_button(self, *args):
        entry2 = self.entry2.get()
        print(entry2)
        # run db query function
        result = db.sql_query(entry2)
        # reconfigure status bar to display entry text
        self.set_statusbar_text(result)
        # add new content to text are
        self.mainwindow_text = str(result)
        # clear out entry field and store current entry
        self.entry2_store(entry2)
        refresh_mainwindow()
        self.entry2_hist_reset()

    def add_button(self, *args):
        entry1 = self.entry1.get()
        print(entry1)
        # run db add function
        result = db.add_name(entry1)
        result = result.fetchall()
        # reconfigure status bar to display entry text
        self.set_statusbar_text(result)
        # add new content to text are
        self.mainwindow_text = str(result)
        refresh_mainwindow()
        # clear out entry field and store current entry
        self.entry1_store(entry1)
        self.entry1_hist_count = 0

    def delete_button(self, *args):
        entry1 = self.entry1.get()
        print(entry1)
        # run db delete command
        result = db.remove_name(entry1)
        result = result.fetchall()
        # reconfigure status bar to display entry text
        self.set_statusbar_text(result)
        # add new content to text are
        self.mainwindow_text = str(result)
        # clear out entry field and store current entry
        self.entry1_store(entry1)
        refresh_mainwindow()

    def enable_main_window(self):
        window = self.mainwindow
        window.config(state=tkinter.NORMAL)

    def disable_main_window(self):
        window = self.mainwindow
        window.config(state=tkinter.DISABLED)

    def main_window_print(self, text):
        # delete existing contents
        window = self.mainwindow
        window.delete(1.0, tkinter.END)
        # add new content to text are
        self.mainwindow_text = str(text)
        refresh_mainwindow()

    def menu_create(self):
        # create menu and set to app with self.config
        main_menu = tkinter.Menu(self)
        self.config(menu=main_menu)
        # create menus
        file_menu = tkinter.Menu(main_menu, tearoff=0)
        main_menu.add_cascade(label="File", menu=file_menu)
        help_menu = tkinter.Menu(main_menu, tearoff=0)
        main_menu.add_cascade(label="Help", menu=help_menu)
        # File submenu options
        file_menu.add_command(label="Copy text", command=simple_copy)
        file_menu.add_separator()
        file_menu.add_command(label="Enable text field", command=self.enable_main_window)
        file_menu.add_command(label="Disable text field", command=self.disable_main_window)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)
        # Help submenu options
        # lambda allows you to pass arguments into the command
        help_menu.add_command(label="NAME_table creation", command= lambda: self.main_window_print(hp.table_help(1)))
        help_menu.add_separator()
        help_menu.add_command(label="SELECT:1", command= lambda: self.main_window_print(hp.select_help(1)))
        help_menu.add_command(label="SELECT:2", command= lambda: self.main_window_print(hp.select_help(2)))
        help_menu.add_command(label="DELETE:1", command= lambda: self.main_window_print(hp.delete_help(1)))
        help_menu.add_command(label="INSERT:1", command= lambda: self.main_window_print(hp.insert_help(1)))
        help_menu.add_command(label="CREATE TABLE:1", command= lambda: self.main_window_print(hp.table_help(2)))
        help_menu.add_separator()
        help_menu.add_command(label="List tables", command= lambda: self.main_window_print(hp.table_help(3)))
        help_menu.add_command(label="Table info", command= lambda: self.main_window_print(hp.table_help(4)))

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
