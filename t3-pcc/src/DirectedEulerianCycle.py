class DirectedEulerianCycle:
    def __init__(self, graph):
        self.graph = graph
        self.cycle = []

        if graph.is_balanced():
            self._find_cycle()

    def _find_cycle(self):
        adj_copy = [list(edges) for edges in self.graph.adj]

        stack = []
        circuit = []

        v = 0
        stack.append(v)

        while stack:
            if adj_copy[v]:
                stack.append(v)
                edge = adj_copy[v].pop()
                v = edge.to_vertex()
            else:
                circuit.append(v)
                v = stack.pop()

        self.cycle = circuit[::-1]

    def get_cycle(self):
        return self.cycle