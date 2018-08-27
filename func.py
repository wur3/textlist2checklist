class Functions:
    def extract(filename):
        item_list = []
        textfile = open(filename, 'r')
        for line in textfile.readlines():
            item_list.append(line.strip())
        textfile.close()
        return item_list

    def save(item_list, filename):
        textfile = open(filename, 'w')
        for line in item_list:
            textfile.write() #thats how you write to a file
        textfile.close()
