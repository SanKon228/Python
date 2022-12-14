class Graph:
    
    def __init__(self, matrix):
        self.matrix = matrix

    def hanging(self):
        counter = 0
        
        for i in self.matrix:
            if sum(i) == 1:
                counter += 1
                
        return counter


if __name__ == "__main__":
    data=[[0,1],[1,0]]
    graph = Graph(data)
    print(graph.hanging())
    data=[[0,1,1],[1,0,1],[1,1,0]]
    graph = Graph(data)
    print(graph.hanging())