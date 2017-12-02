"""
Assignment for Graphs
"""


class MyGraph(object):
    """
    MyGraph Class Object
    """
    def __init__(self, filename):
        """
        Initialization of MyGraph
        """
        f = open(filename, 'r')
        self.adjlist = []
        numv = int(f.readline())
        for x in range(numv):
            self.adjlist.append((x+1, []))
        numed = int(f.readline())
        for x in range(numed):
            connection = f.readline()
            fi = int(connection[0])
            sec = int(connection[2])
            self.adjlist[fi-1][1].append(sec)
            self.adjlist[sec-1][1].append(fi)
        f.close()

    def conn_components(self):
        """
        Returns List of Lists
        """
        cc = []
        for i in range(len(self.adjlist)):
            v = self.adjlist[i]
            found = False
            for l in cc:
                if v[0] in l:
                    found = True
                    break
            if not found:
                cc.append([])
                cc[-1] = self.dfs(v[0], cc[-1])
        for i in range(len(cc)):
            cc[i] = sorted(cc[i])
        return sorted(cc)

    def dfs(self, node, l):
        """
        Helper Function for
        conn_components
        """
        if node in l:
            return l
        l.append(node)
        for v in self.adjlist[node-1][1]:
            self.dfs(v, l)
        return l

    def dcolor(self, node, l, color):
        """
        Colors Vertices
        Helper Function for bicolor
        """
        for i in range(len(l)):
            if node is l[i][0]:
                if l[i][1] is not color:
                    return False
                else:
                    return True
        l.append((node, color))
        for v in self.adjlist[node-1][1]:
            if not self.dcolor(v, l, (color+1) % 2):
                return False
        return True

    def bicolor(self):
        """
        Returns Boolean If Bicolorable
        """
        cc = self.conn_components()
        for comp in cc:
            if len(comp) > 0:
                if not self.dcolor(comp[0], [], 0):
                    return False
        return True
