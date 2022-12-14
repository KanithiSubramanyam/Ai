class Node():
    def __init__(self,graph,vertex,hval):
        self.graph = graph
        self.vertex = vertex
        self.hval = hval
    def genChild(self):
        children =[]
        for ch_vertex in range(0,len(self.graph)):
            if self.graph[self.vertex][ch_vertex] != 0:
                child = Node(self.graph,ch_vertex,0)
                children.append(child)
        return children
class HC():
    def __init__(self,graph,heu,start,stop):
        self.graph = graph
        self.heu = heu
        self.start = start
        self.stop = stop
    def process(self):
        Start = Node(self.graph,self.start,self.heu[self.start])
        cur = Start
        print("Path From Start to Goal:")
        while True:
            print(cur.vertex,end=" ")
            if cur.vertex == self.stop: break
            minchild = None
            for child in cur.genChild():
                child.hval = self.graph[cur.vertex][child.vertex] + self.heu[child.vertex]
                if minchild == None or child.hval < minchild.hval:
                    minchild = child
            cur = minchild
if __name__ == "__main__":
    graph = [[0, 2, 9, 4],
             [2, 0, 2, 9],
             [9, 1, 0, 20],
             [4, 9, 2, 0]]
    heu = [9, 11, 0, 2] 
    q = HC(graph,heu,0,2)
    q.process()