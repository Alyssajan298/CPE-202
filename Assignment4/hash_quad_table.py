"""
Implementation of Quadratic Probing
Hash Table
"""
import string


class HashTableQuadPr(object):
    """
    Quadratic Hash Class
    """
    def __init__(self, size=251):
        """
        Initialization of Hash Table
        """
        self.tsize = size
        self.count = 0
        self.hashlist = []
        for i in range(size):
            self.hashlist.append(None)

    def insert(self, key, item):
        """
        Insert Function that takes a key and item
        """
        if self.get_load_fact() + 1/self.tsize > 0.5:
            self.rehash()
        index = self.myhash(key, self.tsize)
        original = index
        count = 0
        total = 0
        if item is not None:
            while self.hashlist[index] != None and self.hashlist[index][0] != key:
                count += 1
                total = count ** 2
                total += original
                total %= self.tsize
                index = total
            if self.hashlist[index] == None:
                self.hashlist[index] = ((key, [item]))
                self.count += 1
            elif self.hashlist[index] is not None and item not in self.hashlist[index][1]:
                self.hashlist[index][1].append(item)
        else:
            while self.hashlist[index] is not None:
                count += 1
                total = count ** 2
                total += original
                total %= self.tsize
                index = total
            self.hashlist[index] = (key, None)
            self.count += 1

    def contains(self, key):
        """
        Helper Function
        Checks if Key is Contained
        """
        index = self.myhash(key, self.tsize)
        original = index
        count = 0
        total = 0
        while self.hashlist[index] != None and self.hashlist[index][0] != key:
            count += 1
            total = count ** 2
            total += original
            total %= self.tsize
            index = total
        return self.hashlist[index] != None and self.hashlist[index][0] == key

    def get_lines(self, key):
        """
        Uses given key to find and return the item, key pair
        """
        pair = self.get(key)
        return pair[1]

    def get(self, key):
        """
        Helper Function
        Checks if Key is Contained
        """
        index = self.myhash(key, self.tsize)
        original = index
        count = 0
        total = 0
        while self.hashlist[index] != None and self.hashlist[index][0] != key:
            count += 1
            total = count ** 2
            total += original
            total %= self.tsize
            index = total
        if self.hashlist[index] != None and self.hashlist[index][0] == key:
            return self.hashlist[index]
    
    def rehash(self):
        """
        Rehases the Hash Table
        to accomodate for size
        """
        oldhash = self.hashlist
        newhash = HashTableQuadPr(self.tsize * 2 + 1)
        self.tsize = newhash.tsize
        self.count = 0
        self.hashlist = []
        for i in range(self.tsize):
            self.hashlist.append(None)
        for pair in oldhash:
            if pair is None:
                continue
            elif pair[1] is None:
                self.insert(pair[0], None)
            elif len(pair[1]) > 1:
                for linenum in pair[1]:
                    self.insert(pair[0], linenum)
            else:
                self.insert(pair[0], pair[1])

    def read_stop(self, filename):
        """
        Read Stop Words and Hashes into Table
        """
        f = open(filename, 'r')
        while True:
            word = f.readline()
            if word:
                if word.endswith("\n"):
                    word = word[:-1]
                self.insert(word, None)
            else:
                break
        f.close()

    def read_file(self, filename, stoptable):
        """
        Read File, Hashes into Table, and Filters Stop Words
        """
        f = open(filename)
        skip = True
        num = 1
        word = ''
        while True:
            character = f.read(1)
            if not character:
                break
            elif character is "'":
                pass
            elif character in string.ascii_letters or character in string.digits:
                word = word + character
                skip = False
            elif not skip or character is '\n':
                skip = True
                self.decide_to_insert_conditionally(word, stoptable, num)
                if character is '\n':
                    num += 1
                word = ''
        self.decide_to_insert_conditionally(word, stoptable, num)
        f.close()

    def decide_to_insert_conditionally(self, word, stoptable, num):
        """
        Helper Function For
        Read_File
        """
        if len(word) is 0:
            return
        try:
            float(word)
        except:
            if stoptable is None or not stoptable.contains(word.lower()):
                self.insert(word.lower(), num)

    def get_tablesize(self):
        """
        Returns Size of Hash Table
        """
        return self.tsize

    def save_concordance(self, outputfilename):
        """
        Saves Concordance
        """
        ofile = open(outputfilename, "w")
        firstline = True
        sortedlist = []
        for tup in self.hashlist:
            if tup is not None:
                sortedlist.append(tup)
        sortedlist = sorted(sortedlist)
        for tup in sortedlist:
            if firstline:
                firstline = False
            else:
                ofile.write("\n")
            ofile.write(tup[0] + ":")
            for num in tup[1]:
                ofile.write("\t" + str(num))
        ofile.close()

    def get_load_fact(self):
        """
        Returns Load Factor
        """
        return self.count / self.tsize

    def myhash(self, key, table_size):
        """
        Returns Hash Value
        """
        add = 0
        for cont in range(min(len(key), 8)):
            add = 31*add + ord(key[cont])
        return add % table_size
