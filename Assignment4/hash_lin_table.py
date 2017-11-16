"""
Implementation of Linear Probing
Hash Table
"""
import string


class HashTableLinPr(object):
    """
    Linear Hash Class
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
        i = 0
        if item is not None:
            if self.duplicate(key):
                while i < len(self.hashlist):
                    if self.hashlist[i] is not None:
                        if self.hashlist[i][0] == key:
                            self.hashlist[i][1].append(item)
                            break
                    i += 1
                    i %= self.tsize
            else:
                while self.hashlist[index] is not None:
                    index += 1
                    index %= self.tsize
                self.hashlist[index] = ((key, [item]))
        else:
            while self.hashlist[index] is not None:
                index += 1
                index %= self.tsize
            self.hashlist[index] = (key, None)
        self.count += 1

    def duplicate(self, key):
        """
        Helper Function
        Checks for Duplicates
        """
        index = self.myhash(key, self.tsize)
        original = self.myhash(key, self.tsize)
        hashsize = self.tsize
        searchlist = self.hashlist
        while index < hashsize:
            if searchlist[index] is not None:
                if (searchlist[index])[0] == key:
                    return True
            index += 1
            index %= self.tsize
            if index == original:
                return False

    def contains(self, key):
        """
        Helper Function
        Checks if Key is Contained
        """
        index = self.myhash(key, self.tsize)
        original = self.myhash(key, self.tsize)
        hashsize = self.tsize
        searchlist = self.hashlist
        while index < hashsize:
            if searchlist[index] is not None:
                if (searchlist[index])[0] == key:
                    return True
            index += 1
            index %= self.tsize
            if index == original:
                return False

    def get_lines(self, key):
        """
        Uses given key to find and return the item, key pair
        """
        pair = self.get(key)
        return pair[1]

    def get(self, key):
        """
        Returns
        Pair
        """
        index = self.myhash(key, self.tsize)
        original = self.myhash(key, self.tsize)
        hashsize = self.tsize
        searchlist = self.hashlist
        while index < hashsize:
            if searchlist[index] is not None:
                if (searchlist[index])[0] == key:
                    return (key, searchlist[index][1])
            index += 1
            index %= self.tsize
            if index == original:
                raise LookupError

    def rehash(self):
        """
        Rehases the Hash Table
        to accomodate for size
        """
        oldhash = self.hashlist
        newhash = HashTableLinPr(self.tsize * 2 + 1)
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
            elif not skip:
                skip = True
                self.decide_to_insert_conditionally(word, stoptable, num)
                if character is '\n':
                    num += 1
                word = ''
        self.decide_to_insert_conditionally(word, stoptable, num)
        f.close()

    def decide_to_insert_conditionally(self, word, stoptable, num):
        try:
            float(word)
        except:
            if stoptable is None or not stoptable.contains(word):
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
