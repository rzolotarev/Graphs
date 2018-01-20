from queue import Queue

from Graph.abstract import *

def topologicalSort(graph):
    queue = Queue()
    indegreeMap = {}

    for i in range(graph.numVertices):
        indegreeMap[i] = graph.get_indegree(i)

        if indegreeMap[i] == 0:
            queue.put(i)

    sorted_list = []
    while not queue.empty():

        vertex = queue.get()
        sorted_list.append(vertex)

        for v in graph.get_adjacent_vertices(vertex):
            indegreeMap[v] = indegreeMap[v] - 1

            if(indegreeMap[v] == 0):
                queue.put(v)
    
    if len(sorted_list) != graph.numVertices:
        raise ValueError("Grapth has a cycle")
    
    print(sorted_list)


