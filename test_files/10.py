import tkinter


def doNothing():
    print("Nothing")

root = tkinter.Tk()


# Main menu
mymenu = tkinter.Menu(root)
root.config(menu=mymenu)

subMenu = tkinter.Menu(mymenu, tearoff=0)
mymenu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New Project...", command=doNothing)
subMenu.add_command(label="New...", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Preferences", command=doNothing)

editMenu = tkinter.Menu(mymenu, tearoff=0)
mymenu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Do nothing", command=doNothing)

# The toolbar
toolbar = tkinter.Frame(root, bg="blue")

insertButton = tkinter.Button(toolbar, text="Insert", command=doNothing)
insertButton.pack(side=tkinter.LEFT, padx=2, pady=2)
printButton = tkinter.Button(toolbar, text="Print", command=doNothing)
printButton.pack(side=tkinter.LEFT, padx=2, pady=2)

toolbar.pack(side=tkinter.TOP, fill=tkinter.X)



root.mainloop()