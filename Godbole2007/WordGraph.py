from collections import defaultdict

class Node:
    def __init__(self, name, depth=0, node_type='candidate', polarity=1, score=0):
        self.name = name
        self.depth = depth
        self.node_type = node_type
        self.polarity=polarity
        self.score=score

class Graph(object):
    def  __init__(self, connections, directed=False):
        self.graph = defaultdict(set)
        self.directed = directed
        self.add_connections(connections)


    def add_connections(self, connections):
        for node_1, node_2 in connections:
            self.add(node_1, node_2)

    def add(self, node_1, node_2):
        self.graph[node_1].add(node_2)

        if not self.directed:
            self.graph[node_2].add(node_1)

    def remove(self, node):
        for n, cxns in self.graph.items():
            try:
                cxns.remove(node)
            except KeyError:
                pass
        try:
            del self.graph[node]
        except KeyError:
            pass

    def is_connected(self, node_1, node_2):
        return node_1 in self.graph and node_2 in self.graph[node_1]