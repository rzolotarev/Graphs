class Node:
    def __init__(self, vertexId):
        self.vertexId = vertexId
        self.adjacence_set = set()
    
    def add_edge(self, v):
        if self.vertexId == v:
            raise ValueError("The vertex %d cannot be adjacent to itseldf" %v)

        self.adjacence_set.add(v)

    def get_adjacent_vertices(self):
        return sorted(self.adjacence_set)