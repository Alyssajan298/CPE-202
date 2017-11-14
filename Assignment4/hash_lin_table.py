"""
Implementation of Linear Probing
Hash Table
"""
class HashTableLinPr:
    """
    Linear Hash Class
    """
    def __init__(self, size):
        """
        Initialization of Hash Table
        """
        self.tsize = size
        self.count = 0
        self.hashlist = []

    def read_stop(self, filename):
        """
        Read Stop Words and Hashes into Table
        """
        pass

    def read_file(self, filename, stoptable):
        """
        Read File, Hashes into Table, and Filters Stop Words
        """
        pass

    def get_tablesize(self):
        """
        Returns Size of Hash Table
        """
        pass

    def save_concordance(self, outputfilename):
        """
        Saves Concordance
        """
        pass

    def get_load_fact(self):
        """
        Returns Load Factor
        """
        pass

    def myhash(self, key, table_size):
        """
        Returns Hash Value
        """
        pass
