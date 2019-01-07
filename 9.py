import tkinter


def doNothing():
    print("Nothing")

root = tkinter.Tk()

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

root.mainloop()