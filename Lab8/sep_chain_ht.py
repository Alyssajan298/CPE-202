"""
Lab8 Separate Chaining Hash Table
"""


class MyHashTable(object):
    """
    Class to Create a Separate Chaining Hash Table
    """
    def __init__(self, table_size=11):
        """
        Initialize the Hash Table
        """
        self.tsize = table_size
        self.count = 0
        self.hashlist = []
        self.collide = 0
        for i in range(table_size):
            self.hashlist.append([])

    def insert(self, key, item):
        """
        Insert Function that takes a key and item
        """
        if self.load_factor() == 1.5:
            self.rehash()
        index = key % self.tsize
        if self.duplicate(key):
            for i in self.hashlist[index]:
                if i[0] == key:
                    i[1] = item
                    self.collisions += 1
        else:
            if len(self.hashlist[index]) > 0:
                self.collisions += 1
            self.hashlist[index].append((key, item))
        self.count += 1

    def rehash(self):
        """
        Rehases the Hash Table
        to accomodate for size
        """
        oldhash = self.hashlist
        newhash = MyHashTable(self.tsize * 2 + 1)
        self.tsize = newhash.tsize
        self.count = 0
        self.hashlist = []
        for i in range(self.tsize):
            self.hashlist.append([])
        for index0 in range(len(oldhash)):
            for index1 in (oldhash)[index0]:
                index = index1[0] % self.tsize
                self.hashlist[index].append((index1[0], index1[1]))
                self.count += 1

    def duplicate(self, key):
        """
        Helper Function
        Checks for Duplicates
        """
        index = key % self.tsize
        i = 0
        hashsize = len(self.hashlist[index])
        searchlist = self.hashlist[index]
        while i < hashsize:
            if (searchlist[i])[0] == key:
                return True
        return False

    def get(self, key):
        """
        Uses given key to find and return the item, key pair
        """
        index = key % self.tsize
        i = 0
        hashsize = len(self.hashlist[index])
        searchlist = self.hashlist[index]
        while i < hashsize:
            if (searchlist[i])[0] == key:
                return searchlist[i]
            i += 1
        raise LookupError

    def remove(self, key):
        """
        Removes item, key pair and returns it
        """
        index = key % self.tsize
        i = 0
        hashsize = len(self.hashlist[index])
        searchlist = self.hashlist[index]
        while i < hashsize:
            if (searchlist[i])[0] == key:
                temp = searchlist[i]
                del searchlist[i]
                return temp
            i += 1
        raise LookupError

    def size(self):
        """
        Returns number of pairs in the Hash Table
        """
        return self.count

    def load_factor(self):
        """
        Returns current load factor
        """
        return self.count / self.tsize

    def collisions(self):
        """
        Returns number of collisions during insertions
        """
        return self.collide
