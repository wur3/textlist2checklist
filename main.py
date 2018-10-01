from tkinter import *
from func import Functions

### Section I: txt parsing
file = "list.txt"

# file = input("Name of .txt file:\n")
list = Functions.extract(file)

### Section II: Tkinter
root = Tk()
root.title("Check List")
Label(root, text = "Welcome to textlist2checklist!", padx = 10, \
                        pady = 4, justify = CENTER).pack()
buttons = []
for item in list:
    checkvar = BooleanVar()
    cb = Checkbutton(root, text = item, variable = checkvar, \
                        anchor = 'w', height = 1, width = 15)
    cb.pack()
    buttons.append([cb, checkvar])
Button(root, text = "Save", \
    command = lambda: Functions.save(buttons, "list.txt"), \
    padx = 5, pady = 2).pack()
root.mainloop()
