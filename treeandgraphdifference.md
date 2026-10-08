"""
1. Small Tree
        A
       / \
      B   C
     / \
    D   E
A is the root.
B and C are children of A.
D and E are children of B.
This is a tree because there is a single path between any two nodes.
2. Small Graph
      A ----- B
      |       |
      |       |
      C ----- D

Edges:

A-B
A-C
B-D
C-D

Unlike a tree, a graph can have cycles and multiple possible paths.
"""

from collections import deque

tree = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": [],
    "D": [],
    "E": []
}

queue = deque(["A"])

while queue:
    node = queue.popleft()
    print(node, end=" ")

    for child in tree[node]:
        queue.append(child)

"""
Output:

A B C D E

This is Breadth-First Search (BFS) because it visits nodes level by level:

Level 1: A
Level 2: B C
Level 3: D E
"""

"""
Small Graph
      A ----- B
      |       |
      |       |
      C ----- D
A, B, C, and D are nodes (vertices).
A is connected to B and C.
B is connected to A and D.
C is connected to A and D.
D is connected to B and C.
The connections between the nodes are called edges.
The edges are A-B, A-C, B-D, and C-D.
This is a graph because the nodes are connected through edges and there can be multiple paths between two nodes.
For example, there are two paths from A to D: A → B → D and A → C → D.
"""
graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": [],
    "D": [],
    "E": []
}

def dfs(node):
    print(node, end=" ")

    for child in graph[node]:
        dfs(child)

dfs("A")


""" 
Output:

A B D E C
"""