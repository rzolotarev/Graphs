from queue import Queue
import numpy as np

from Graph.abstract import *

def breadth_first(graph, start = 0):

    queue = Queue()
    queue.put(start)

    visited = np.zeros(graph.numVertices)

    while not queue.empty():
        vertex = queue.get()

        if visited[vertex] == 1:
            continue

        print("Visit:", vertex)

        visited[vertex] = 1

        for i in graph.get_adjacent_vertices(vertex):
            if visited[i] != 1:                
                queue.put(i)

