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

            # remove the item from the stack
            stack.pop()

        else:
            # check each edge
            for vertext_at_edge in graph[vertex]:
                # add the vertices at the edges to the stack
                stack.append(vertext_at_edge)

            # then mark the vertex as visited
            visited.append(vertex)


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

    while len(queue) > 0:
        
        # get the item from the front of the queue
        vertex = queue[0]
        # if there are no edge or this vertex has already been visited
        if len(graph[vertex]) == 0 or vertex in visited:
            # remove the item from the stack
            queue.remove(vertex)

        else:
            # check each edge
            for vertex_at_edge in graph[vertex]:
                if vertex_at_edge not in visited:
                    # add the vertices at the edges to the stack
                    queue.append(vertex_at_edge)

            # then mark the vertex as visited
            visited.append(vertex)
            queue.remove(vertex)

    


