"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    # def add_undirected_edge(self, v1, v2):
    #     """
    #     Add an undirected edge to the graph.
    #     """
    #     if v1 in self.vertices and v2 in self.vertices:
    #         self.vertices[v1].add(v2)
    #         self.vertices[v2].add(v1)
    #     else:
    #         raise ValueError("vertex does not exist")


    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise ValueError("vertex does not exist")




    def get_neighbors(self, vertex_id):
        """-
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            raise ValueError("vertex does not exist")




    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        q.enqueue(starting_vertex)
        visited = set()

        while q.size() > 0:
            # dequeue the first vertext
            v = q.dequeue()
            # check if it's been visited.. if not, then do this:
            if v not in visited:
                # mark as visited
                print(v)
                visited.add(v)
                # enqueue all its neighbors
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)



    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        s.push(starting_vertex)
        visited = set()

        while s.size() > 0: 
            v = s.pop()
            if v not in visited:
                print(v)
                visited.add(v)
                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)




    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        if starting_vertex in visited:
            return
        else: 
            visited.add(starting_vertex)
            print(starting_vertex)
            for neighbor in self.get_neighbors(starting_vertex):
                if neighbor not in visited:
                    self.dft_recursive(neighbor, visited)
    #we create visited parameter (set as None initially) which is a set (obj), that tells us if we've seen something already
    # first we check if visited has been made - if not, then create a new set
    # then we check if the vertex we're looking at has alreayd been visited 
        # if it has been, then return
    # if we haven't seen the vertex yet (meaning it isn't in visited set)
        # we will add it to the set -> print it -> then grab all of it's neighbors (EDGES)
        # for each of its neighbors (EDGES) we will recursively call the function again





    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()
        q.enqueue([starting_vertex])
        visited = set()

        while q.size() > 0:
            path = q.dequeue()
            last_vertex = path[-1]
            if last_vertex == destination_vertex:
                return path 
            if last_vertex not in visited:
                visited.add(last_vertex)
                for neighbor in self.get_neighbors(last_vertex):
                    copy = path.copy()
                    copy.append(neighbor)
                    q.enqueue(copy)




    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        # why am I using [starting_vertex] instead of starting_vertex?
        s.push([starting_vertex])
        visited = set()

        while s.size() > 0:
            path = s.pop()
            last_vertex = path[-1]
            if last_vertex == destination_vertex:
                return path 
            if last_vertex not in visited:
                visited.add(last_vertex)
                for neighbor in self.get_neighbors(last_vertex):
                    copy = path.copy()
                    copy.append(neighbor)
                    s.push(copy)

        # create an empty queue
        # add a stack to the starting vertex_id to the queue 
        # create an empty set to store visited nodes 
        # while queue is not empty..
            # dequeue, the first path
            # grab the last vertex from the path 
            # check if it's the target 
                # if so, return the path
            # if it has not been visited..
                # mark it as visited
                # then add a path to all neighbors to the back of the queue 
                    # make a copy of the path before adding





    def dfs_recursive(self, starting_vertex, target_value, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        if path is None:
            path = []
        path.append(starting_vertex)
        current_vertex = starting_vertex
        visited.add(starting_vertex)

        if current_vertex == target_value:
            return path
        else: 
            for neighbor in self.get_neighbors(current_vertex):
                copy = path.copy() 
                if neighbor not in visited: 
                    # MISTAKE HERE - NEIGHBOR instead of Current_vertex AND COPY instead of path or path.copy!! 
                    # YOU MUST COPY THE PATH
                    new_path = self.dfs_recursive(neighbor, target_value, visited, copy)
                    if new_path:
                        return new_path 
        return None 












if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
