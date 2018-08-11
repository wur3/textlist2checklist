from tkinter import *
from tkinter import ttk

# Section I: txt parsing
filename = "list.txt"
# filename = input("Name of .txt file:\n")
textfile = open(filename, 'r')
for line in textfile.readlines():
    print(line.strip())

# Section II: Tkinter
root = Tk()
root.title("Check List")
cb = ttk.Checkbutton(root, text = "TEST")
cb.pack()

root.mainloop()
