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
"""
