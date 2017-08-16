"""
Created on Aug 14, 2017

@author: Evan Burton

A graph is an pair G = (V, E)

    V = set of vertices
    E = set of edges
        {v, w} unordered edges
        (v, w) ordered edges

A graph is directed if all edges are unordered.

An undirected graph:

        a----b
        |  / |
        c/---d
        
A directed graph:

        a--->b
        ^    ^
        |    |
        c<---d
        
Applications:
    - Web crawling
    - Social networking
    - Network broadcast
    - Garbage collection
    - Model checking
    - Checking mathematical conjectures
    - Solving puzzles and games
    
Configuration Graph:

 -               
 |               o
 |             /  \
 |           /     \
 |          o       o
 |         /\      /\
 |        o  o    o  o
 -
 
 diameter = height of tree
 
 Graph representation:
 
     Adjacency Lists: 
         - array Adj of |V| linked lists
         - for each vertex u in V, Adj[u] stores u's neighbors
         - Theta(|V|+|E|) space

Implicit representation:
    - Adj(u) is a function
    - v.neighbors() is a method
    - Don't have to store all possible states

#####################################################
#                Breadth First Search               #
#####################################################

Goal: 
    - Visit all nodes reachable from given node s in V
    - Achieve O(|V| + |E|) time
    - Look at nodes reachable in 0 moves, 1 move, 2 moves, etc
    - Avoid duplicates
"""

class Graph():
    def __init__(self, V={}, E=[]):
        self.V = V
        self.E = E
    
    # Adj[u] = {v in V | {u, v} in E}
    # This translates so well to python    
    def adj(self, u):

        Adj = []
        
        for v in self.V:
            if {u, v} in self.E:
                Adj.append(v)
                
        return Adj

    def BFS(self, s):
        
        level = {s:0}
        parent = {s: None}
        i = 1
        frontier = [s]
    
        while frontier:
            next = []
    
            for u in frontier:
               # edge {u, v}
                for v in self.adj(u):
                   # prevent cycles
                    if v not in level:
                       level[v] = i
                       parent[v] = u
                       next.append(v)
            frontier = next
            i += 1
        return level

graph = Graph({'a', 'z', 's', 'x', 'd', 'c', 'f', 'v'},
               [{'a','z'}, {'a', 's'}, {'s', 'x'}, {'x', 'd'},
                {'x', 'c'}, {'c','d'}, {'c', 'v'}, {'d', 'f'},
                {'c', 'f'}, {'v', 'f'}])

print(graph.BFS('s'))

"""

a-----s     d-----f
|     |   / |   / |
|     |/    |/    |
z     x-----c-----v


level[s] = 0
level[a] = 1
level[x] = 1
    - Adj[a] = [s, z] but s in level[0]
        - So z is in level 2
    - Adj[x] = [s, c, d] but s in level[0]
        - Add c and d to level 2
level[z] = 2
level[c] = 2
level[d] = 2
    - Repeat above
level[f] = 3
level[v] = 3

#####################################################
#                Shortest Paths                     #
#####################################################

v <- parent[v]
  <- parent[ parent[v] ]
  ...
  <- s

is a shortest path from s to v.

"""
