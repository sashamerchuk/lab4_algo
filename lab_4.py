from collections import defaultdict


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)
        self.visited = []
        self.s_graph = []
    def dfs(self,node):
        if node not in self.visited:
            self.visited.append(node)
            for neighbour in self.graph[node]:
                self.dfs(neighbour)



    def component(self):
        for key in self.visited:
            if key in self.graph:
                self.graph.pop(key)
        for key in self.graph:
            self.s_graph.append(key)

    def find_pairs(self):
        f_girls, f_boys, s_girls, s_boys = [], [], [], []
        for i in range(len(self.visited)):
            if self.visited[i] % 2 == 0:
                f_girls.append(self.visited[i])
            else:
                f_boys.append(self.visited[i])
        for i in range(len(self.s_graph)):
            if self.s_graph[i] % 2 == 0:
                s_girls.append(self.s_graph[i])
            else:
                s_boys.append(self.s_graph[i])
        print("Pairs :",len(f_girls) * len(s_boys) + len(f_boys) * len(s_girls))

    def read(self, graph_file_path):
        try:
            with open(graph_file_path, 'r') as graph_file:
                for line in graph_file:
                    u, v = line.split()
                    self.graph[int(u)].append(int(v))
                    self.graph[int(v)].append(int(u))
        except Exception as exception:
            print("Error : ", exception)


def main():
    g = Graph()
    print("DFS")
    g.read("file_1")
    g.dfs(5)
    g.component()
    g.find_pairs()


main()