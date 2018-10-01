from tkinter import *

class Functions:
    def extract(filename):
        item_list = []
        textfile = open(filename, 'r')
        for line in textfile.readlines():
            item_list.append(line.strip())
        textfile.close()
        return item_list

    def save(widget_list, filename):
        #textfile = open(filename, 'w')
        for widget in widget_list:

            print (widget[0].cget("text"))
            print (widget[1].get())
            #textfile.write() #thats how you write to a file
        #textfile.close()
