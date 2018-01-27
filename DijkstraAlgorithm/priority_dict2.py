class PriorityQueue:

    def __init__(self):
        self.queue = {}
    
    def append(self, vertex, distance):
        self.queue[vertex] = distance
    
    def pop(self):        
        my_dict = self.queue
        min_key = min(my_dict.keys(), key=(lambda k: my_dict[k]))
        my_dict.pop(min_key)
        return min_key

    def keys(self):
        return self.queue