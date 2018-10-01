from tkinter import *
from tkinter import filedialog

class Checklist:
    def __init__(self, root):
        #file dialog for file to read from
        self.filename = filedialog.askopenfilename(initialdir = "/Desktop/", \
            title = "Select file",filetypes = (("Text File", "*.txt"),("All Files","*.*")))

        if not self.filename:
            print ("No file location chosen. Program terminated.")
            raise SystemExit

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

        #List of Checkbuttons
        self.make_list()

        #Clear button
        self.clear_button = Button(self.root, text = "Clear", \
            command = lambda: self.clear(), \
            padx = 5, pady = 2)
        self.clear_button.pack()

        #Save button
        self.save_button = Button(self.root, text = "Save", \
            command = lambda: self.save(), \
            padx = 5, pady = 2)
        self.save_button.pack()

    #Returns list of strings from filename
    def extract(self):
        list = []
        textfile = open(self.filename, 'r')
        for line in textfile.readlines():
            list.append(line.strip())
        textfile.close()
        return list

    #Adds a checkbutton and checkbox variable for each item in item_list
    def make_list(self):
        for item in self.item_list:
            checkvar = BooleanVar()
            cb = Checkbutton(self.root, text = item, variable = checkvar, \
                                anchor = 'w', height = 1, width = 15)
            cb.pack()
            self.buttons.append(cb)
            self.cb_val.append(checkvar)

    def clear(self):
        for i in range(len(self.cb_val)):
            self.cb_val[i].set(False)


    #Saves current state of checkboxes
    def save(self):
        #textfile = open(filename, 'w')
        for i in range(len(self.buttons)):
            #if checked
            if (self.cb_val[i].get()):
                print ("[X] " + self.buttons[i].cget("text"))
            else:
                print ("[ ] " + self.buttons[i].cget("text"))
            #textfile.write() #thats how you write to a file
        #textfile.close()
