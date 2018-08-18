from tkinter import *
#from tkinter import ttk

item_list = []

# Section I: txt parsing
filename = "list.txt"
print("opening list.txt")
# filename = input("Name of .txt file:\n")
textfile = open(filename, 'r')
for line in textfile.readlines():
    item_list.append(line.strip())

# Section II: Tkinter
root = Tk()
root.title("Check List")
Label(root, text = "Welcome to textlist2checklist!", justify = CENTER).pack()
for item in item_list:
    checkvar = BooleanVar()
    cb = Checkbutton(root, text = item, variable = checkvar, \
                        height = 2, width = 10)
    cb.pack()

root.mainloop()
