"""
BREADTH TRAVERSAL IN PYTHON
"""

def breadth_traversal(graph, root_key):
    """
    Pushes each vertex onto the stack,
    and after it has visited each vertex it pops it off the stack
    """
    # track which edges of each vertex have been visited
    visited = []
    
    # initialise the stack, pushing the root vertex onto the stack
    queue = []
    queue.append(root_key)
    print("adding %s" % root_key)

    while len(queue) > 0:
        
        # get the item from the front of the queue
        vertex = queue[0]
        print("checking %s" % vertex)
        # if there are no edge or this vertex has already been visited
        if len(graph[vertex]) == 0 or vertex in visited:

            print("removing %s" % vertex)

            # remove the item from the stack
            queue.remove(vertex)

        else:
            # check each edge
            for vertex_at_edge in graph[vertex]:
                if vertex_at_edge not in visited:
                    print("adding %s" % vertex_at_edge)

                    # add the vertices at the edges to the stack
                    queue.append(vertex_at_edge)

            # then mark the vertex as visited
            visited.append(vertex)
            print("removing %s" % vertex)
            queue.remove(vertex)

    print("vertices have been visited in the following order %s" % visited)
    



print("*** Graph Traversal 1 ***")

'''
page 211 in...
Heathcote, P. M.; Heathcote, R. S. U. (2016).
OCR AS and A Level Computer Science,
PG Online
'''

graph_1 = {
    "A":["C", "B",],
    "B":["K"],
    "C":["F", "D"],
    "D":["G", "H", "E"],
    "E":[],
    "F":["J","G"],
    "G":[],
    "H":[],
    "J":["H"],
    "K":[]
}


breadth_traversal(graph_1, "A")

print("*** END ***")



print("*** Graph Traversal 2 ***")

'''
page 211 in...
Craig and Dave (2016).
OCR A Level Data Structures C,T,A,R Part 2 Graphs,
YouTube
'''

graph_2 = {
    "A":["C", "B"],
    "B":["C","D","E"],
    "C":["F", "D"],
    "D":["H"],
    "E":["D"],
    "F":["G"],
    "G":[],
    "H":[],
}

breadth_traversal(graph_2, "A")

print("*** END ***")


