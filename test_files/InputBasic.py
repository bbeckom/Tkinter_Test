import tkinter


class SampleApp(tkinter.Tk):
    def __init__(self):

        tkinter.Tk.__init__(self)
        self.entry = tkinter.Entry(self)
        self.button = tkinter.Button(self, text="Get Input", command=self.on_button)
        self.button.pack()
        self.entry.pack()

    def on_button(self):
        print(self.entry.get())


app = SampleApp()
app.mainloop()
