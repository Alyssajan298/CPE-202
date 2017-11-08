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
        for i in range(table_size):
            self.hashlist.append([])

    def insert(self, key, item):
        """
        Insert Function that takes a key and item
        """
        if self.count / self.tsize == 1.5:
            self.rehash()
        index = key % self.tsize
        self.hashlist[index].append((key, item))
        self.count += 1

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
        pass

    def size(self):
        """
        Returns number of pairs in the Hash Table
        """
        pass

    def load_factor(self):
        """
        Returns current load factor
        """
        pass

    def collisions(self):
        """
        Returns number of collisions during insertions
        """
        pass
