class Graph:

    def __init__(self, arg):
        self.matrix = arg

    def neigbhours(self, node):
        l = [index for index, val in enumerate(self.matrix[node]) if val == 1]
        return l

    def isWeak(self, node):
        neig = self.neigbhours(node)
        #print(neig)
        for n in neig:
            nn = self.neigbhours(n)
            for nnn in nn:
                if nnn in neig:
                    return False

        return True

n = int(input())

while(n != -1):
    graph = []
    for i in range(n):
        graph.append(list(map(int,input().split())))
    g = Graph(graph)
    for i in range(n):
        #print(i)
        if g.isWeak(i):
            print(i, end=" ")
    print()
    n = int(input())
