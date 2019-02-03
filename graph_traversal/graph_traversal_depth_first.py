"""
DEPTH TRAVERSAL IN PYTHON
"""

def depth_traversal(graph, root_key):
    """
    Pushes each vertex onto the stack,
    and after it has visited each vertex it pops it off the stack
    """
    # track which edges of each vertex have been visited
    visited = []
    
    # initialise the stack, pushing the root vertex onto the stack
    stack = []
    stack.append(root_key)

    while len(stack) > 0:
        
        # get the item from the top of the stack
        vertex = stack[len(stack)-1]
        
        # if there are no edge or this vertex has already been visited
        if len(graph[vertex]) == 0 or vertex in visited:

            print("popping vertex %s" % vertex)

            # remove the item from the stack
            stack.pop()

        else:
            # check each edge
            for vertext_at_edge in graph[vertex]:
                print("vertex %s has edge %s" % (vertex, vertext_at_edge))

                # add the vertices at the edges to the stack
                stack.append(vertext_at_edge)

            # then mark the vertex as visited
            visited.append(vertex)

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

depth_traversal(graph_1, "A")

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

depth_traversal(graph_2, "A")

print("*** END ***")


