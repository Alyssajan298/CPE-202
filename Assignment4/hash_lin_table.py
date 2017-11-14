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
