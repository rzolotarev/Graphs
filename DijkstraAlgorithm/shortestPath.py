from DijkstraAlgorithm.priority_dict2 import *

from Graph.abstract import *

def build_distance_table(graph, source):
    
    distance_table = {}

    for i in range(graph.numVertices):
        distance_table[i] = (None, None)
    
    distance_table[source] = (0, source)

    priority_queue = PriorityQueue()

    priority_queue.append(source,0)        
    
    while len(priority_queue.keys()) > 0:

        current_vertex = priority_queue.pop()        

        current_distance = distance_table[current_vertex][0]

        for neighbor in graph.get_adjacent_vertices(current_vertex):

            distance = current_distance + graph.get_edge_weight(current_vertex, neighbor)

            neighbor_distance = distance_table[neighbor][0]

            if neighbor_distance is None or neighbor_distance > distance:
                distance_table[neighbor] = (distance, current_vertex)                
                priority_queue.append(neighbor, distance)
    
    return distance_table

def shortest_path(graph, source, destination):

    distance_table = build_distance_table(graph, source)
    path = [destination]

    previous_vertex = distance_table[destination][1]

    while previous_vertex is not None and previous_vertex is not source:
        path = [previous_vertex] + path
        previous_vertex = distance_table[previous_vertex][1]

    if previous_vertex is None:
        raise ValueError("There is no path from %d to %d" % (source, destination))
    else:
        print([source] + path)    