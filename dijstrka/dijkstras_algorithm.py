class Vertex():
    def __init__(self, key):
        """ Initial values for the Vertex """
        self.key = key
        """ Default properties """
        self.min_distance_from_start = float("inf")
        self.previous = None
        self.edges = []
        
    def __cmp__(self, other):
        """ Override Compare (Used to prioritise the Vertex in the priority queue """
        return self.cmp(self.min_distance_from_start, other.min_distance_from_start)
    
    def __lt__(self, other):
        """ Override Less Than (Used to prioritise the Vertex in the priority queue """
        selfP = self.min_distance_from_start
        otherP = other.min_distance_from_start
        return selfP < otherP
    
class Edge():
    def __init__(self, weight, startV, targetV):
        """ Initial values for the edge """
        self.weight = weight
        self.startV = startV # vertex
        self.targetV = targetV # vertex


""" Use Python priority queue """
import heapq

def getShortestPath(vertices, startV, target):
    
    """ The priority queue (use headq to order the vertices by distance from start) """
    queue = []
    
    """ start node is zero distance from itself """
    startV.min_distance_from_start = 0
    
    """ add the starting vertex to the priority queue """
    heapq.heappush(queue, startV)
    
    while len(queue) > 0:
        """ get the item with the shorest distance from the start """
        currV = heapq.heappop(queue)
        
        """ check the weight each edge """
        for edge in currV.edges:
            u = edge.startV
            v = edge.targetV
            """ add the weight to the distance from the start for this edge """
            distance = u.min_distance_from_start + edge.weight
            """ checking if new distance is less than distance from the start """
            if distance < v.min_distance_from_start:
                """ the current vertex is now the new path """
                v.previous = u;
                """ update the distance from the start (now the shorter distance) """
                v.min_distance_from_start = distance
                """ add to the priority queue """
                heapq.heappush(queue, v)
    
    """ work through the nodes back to the start """
    node = target
    shortestPath = []
    while node is not None:
        shortestPath.append(node.key)
        node = node.previous
        
    return shortestPath

