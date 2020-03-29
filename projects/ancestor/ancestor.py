import sys 

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # ADDED THIS - it was because it was overriding 47/48
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()


    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise ValueError("vertex does not exist")

# [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
def earliest_ancestor(ancestors, starting_node):
    # step 1 make graph
    g = Graph()
    for member in ancestors:
        parent,child = member
        g.add_vertex(parent)
        g.add_vertex(child)
        # directed edge means pointing A to B in (A,B)
        g.add_edge(child, parent)
            
    print(g.vertices)

    # step 2 - traverse graph
    q = Queue()
    q.enqueue([starting_node])
    visited = set()

    #BIG MISTAKE HERE - Earliest ancestor (if there isn't any - is -1) // and the path will always be 1
    earliest_ancestor = -1
    longest_path = 1

    while q.size() > 0:
        path = q.dequeue()
        current_node = path[-1]
        # take note of these two conditional statements
        if current_node < earliest_ancestor and len(path) >= longest_path or len(path) > longest_path:
            longest_path = len(path)
            earliest_ancestor = current_node 
   
        if current_node not in visited: 
            visited.add(current_node)
            for family_member in g.vertices[current_node]:
                copy_path = path.copy()
                copy_path.append(family_member)
                q.enqueue(copy_path)
    return earliest_ancestor

# check out lines 27, 59, 67 
# if you take out 4, and make 5 point to 2 (2 is parent of 5) and (11 is parent of 8)