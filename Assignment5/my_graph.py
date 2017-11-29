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
        numv = int(f.readline()[0])
        for i in range(numv):
            self.adjlist.append((i+1, []))
        nume = int(f.readline()[0])
        for i in range(nume):
            edge = f.readline().split()
            for i in range(len(edge)):
                if '\n' in edge[i]:
                    edge[i] = edge[i][:-1]
                edge[i] = int(edge[i])
            for x in range(len(edge)):
                index = edge[x] - 1
                for y in range(len(edge)):
                    if x != y:
                        self.adjlist[index][1].append(edge[y])
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
        if node in l:
            return l
        l.append(node)
        for v in self.adjlist[node-1][1]:
            self.dfs(v, l)
        return l

    def bicolor(self):
        """
        Returns Boolean If Bicolorable
        """
        pass
