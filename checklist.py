from tkinter import *

class Checklist:

    def __init__(self, root):
        self.filename = "list.txt"
        #self.filename = input("Name of .txt file:\n")

        # list of Checkbutton objects
        self.buttons = []
        # list of corresponding checkbox values
        self.cb_val = []

        self.root = root
        root.title("Check List")
        self.label = Label(root, text = "Welcome to textlist2checklist!", padx = 10, \
                            pady = 4, justify = CENTER)
        self.label.pack()

        # list of string items extracted from file
        self.item_list = []
        self.item_list = self.extract()
        self.make_list()

        self.save_button = Button(self.root, text = "Save", \
            command = lambda: self.save(), \
            padx = 5, pady = 2)
        self.save_button.pack()

    def extract(self):
        list = []
        textfile = open(self.filename, 'r')
        for line in textfile.readlines():
            list.append(line.strip())
        textfile.close()
        return list

    def make_list(self):
        for item in self.item_list:
            checkvar = BooleanVar()
            cb = Checkbutton(self.root, text = item, variable = checkvar, \
                                anchor = 'w', height = 1, width = 15)
            cb.pack()
            self.buttons.append(cb)
            self.cb_val.append(checkvar)

    def save(self):
        #textfile = open(filename, 'w')
        for i in range(len(self.buttons)):
            print (self.buttons[i].cget("text"))
            print (self.cb_val[i].get())
            #textfile.write() #thats how you write to a file
        #textfile.close()
