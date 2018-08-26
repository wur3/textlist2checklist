class Functions:
    def extract(filename):
        item_list = []
        textfile = open(filename, 'r')
        for line in textfile.readlines():
            item_list.append(line.strip())
        return item_list

    def save(filename):
        textfile = open(filename, 'r')
        for line in textfile.readlines():
            pass
