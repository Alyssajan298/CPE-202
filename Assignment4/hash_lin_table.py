"""
Implementation of Linear Probing
Hash Table
"""


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
        if item is not None:
            if self.duplicate(key):
                for i in range(len(self.hashlist)):
                    if self.hashlist[i][0] == key:
                        self.hashlist[i][1].append(item)
            else:
                while self.hashlist[index] is not None:
                    index += 1
                    index %= self.tsize
                self.hashlist[index] = ((key, [item]))
        else:
            while self.hashlist[index] is not None:
                index += 1
                index %= self.tsize
            self.hashlist[index] = key
        self.count += 1

    def duplicate(self, key):
        """
        Helper Function
        Checks for Duplicates
        """
        index = self.myhash(key, self.tsize)
        hashsize = len(self.hashlist)
        searchlist = self.hashlist
        while index < hashsize:
            if (searchlist[index])[0] == key:
                return True
            index += 1
            index %= self.tsize
        return False

    def contains(self, key):
        """
        Helper Function
        Checks if Key is Contained in Hash
        """
        index = self.myhash(key, self.tsize)
        hashsize = len(self.hashlist)
        searchlist = self.hashlist
        while index < hashsize:
            if (searchlist[index])[0] == key:
                return True
            index += 1
            index %= self.tsize
        return False

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
            if len(pair[1]) > 1:
                for linenum in pair[1]:
                    self.insert(pair[0], linenum)
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
        pass

    def get_tablesize(self):
        """
        Returns Size of Hash Table
        """
        return self.tsize

    def save_concordance(self, outputfilename):
        """
        Saves Concordance
        """
        pass

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
            add += 31*add + ord(key[cont])
        return add % table_size
