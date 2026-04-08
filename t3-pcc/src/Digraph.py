class Digraph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range(V)]
        self.in_degree = [0] * V
        self.out_degree = [0] * V

    def add_edge(self, edge):
        v = edge.from_vertex()
        w = edge.to_vertex()

        self.adj[v].append(edge)
        self.out_degree[v] += 1
        self.in_degree[w] += 1

    def get_adj(self, v):
        return self.adj[v]

    def is_balanced(self):
        for v in range(self.V):
            if self.in_degree[v] != self.out_degree[v]:
                return False
        return True