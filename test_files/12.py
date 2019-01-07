import tkinter
import tkinter.messagebox


root = tkinter.Tk()

tkinter.messagebox.showinfo('Window Title', "test text")

answer = tkinter.messagebox.askquestion('Question 1', 'Are you a person?')

if answer == 'yes':
    print('yes')
elif answer == 'no':
    print('no')

root.mainloop()
