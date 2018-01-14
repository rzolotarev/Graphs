from queue import Queue
import numpy as np

from Graph.abstract import *

def depth_first(graph, visited, current = 0):
    if visited[current] == 1:
        return

    visited[current] = 1

    print("Visited", current)

    for vertex in graph.get_adjacent_vertices(current):
        depth_first(graph, visited, vertex)

