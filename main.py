from tkinter import *

item_list = []

### Section I: txt parsing
filename = "list.txt"

# filename = input("Name of .txt file:\n")
textfile = open(filename, 'r')
for line in textfile.readlines():
    item_list.append(line.strip())

### Section II: Tkinter
root = Tk()
root.title("Check List")
Label(root, text = "Welcome to textlist2checklist!", padx = 10, \
                        pady = 4, justify = CENTER).pack()
for item in item_list:
    checkvar = BooleanVar()
    cb = Checkbutton(root, text = item, variable = checkvar, \
                        anchor = 'w', height = 1, width = 15)
    cb.pack()
Button(root, text = "Save", padx = 5, pady = 2).pack()
root.mainloop()
