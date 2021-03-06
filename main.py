
from Graph.adjacencyMatrixGraph import AdjacencyMatrixGraph

from Graph.adjacencySetGraph import AdjacencySetGraph 

from Traversal.breadthFirst import *

from Traversal.depthFirst import *

from TopologicalSort.topologicalSort import *

# from UnweightShortestPath.shortestPath import *

from DijkstraAlgorithm.shortestPath import *

# g = AdjacencyMatrixGraph(4, directed=True)

# g.add_edge(0,1)
# g.add_edge(0,2)
# g.add_edge(2,3)

# for i in range(4):
#     print("Adjacent to: ", i, g.get_adjacent_vertices(i))

# for i in range(4):
#     print("Indegree: ", i, g.get_indegree(i))

# g.display()

# g = AdjacencySetGraph(4, directed=True)

# g.add_edge(0,1)
# g.add_edge(0,2)
# g.add_edge(2,3)

# for i in range(4):
#     print("Adjacent to: ", i, g.get_adjacent_vertices(i))

# for i in range(4):
#     print("Indegree: ", i, g.get_indegree(i))

# g.display()
g = AdjacencyMatrixGraph(9, directed = False)

g.add_edge(0, 1, 1)
g.add_edge(1, 2, 2)
g.add_edge(1, 3, 6)
g.add_edge(2, 3, 2)
g.add_edge(1, 4, 3)
g.add_edge(3, 5, 1)
g.add_edge(5, 4, 5)
g.add_edge(3, 6, 1)
g.add_edge(6, 7, 1)
g.add_edge(0, 7, 8)


# breadth_first(g,2)
# visited = np.zeros(g.numVertices)
# depth_first(g, visited)

# topologicalSort(g)

shortest_path(g, 0, 6)
shortest_path(g, 4, 7)
shortest_path(g, 7, 0)