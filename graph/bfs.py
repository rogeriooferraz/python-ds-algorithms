"""
Copyright (c) 2024 Rogerio O. Ferraz <rogerio.o.ferraz@gmail.com>

MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.                                                           
"""

from collections import deque
from graph import Graph


def bfs_traversal(adj_list, orig_node):
    visited = [orig_node]
    queue = deque(orig_node)
    while queue:
        inode = queue.popleft()
        for jnode in [ adj_v for adj_v in adj_list[inode] if adj_v not in visited ]:
            visited.append(jnode)
            queue.append(jnode)
    return visited


def bfs_path_list(adj_list, orig_vertex, dest_vertex):
    queue = deque([(orig_vertex, [orig_vertex])])
    while queue:
        (inode, path) = queue.popleft()
        for jnode in [ adj_v for adj_v in adj_list[inode] if adj_v not in path ]:
            if jnode == dest_vertex:
                yield path + [jnode]
            else:
                queue.append((jnode, path + [jnode]))


def bfs_shortest_path(adj_list, orig_vertex, dest_vertex):
    try:
        return next(bfs_path_list(adj_list, orig_vertex, dest_vertex))
    except StopIteration:
        return None


# -----------------------------------------------------------------------------
# Graph
# -----------------------------------------------------------------------------

print("Graph:")

graph_adj_list = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

g = Graph(graph_adj_list)
print("\t", g, "\n")

# -----------------------------------------------------------------------------
# Traversal using Breadth-First Search (BFS)
# -----------------------------------------------------------------------------

print("Traversal using Breadth-First Search (BFS):\n")

print(f'using class method\t: {g.bfsTraversal("A")}')
print("using function\t\t: %s\n" % bfs_traversal(graph_adj_list, "A"))

# -----------------------------------------------------------------------------
# Path List
# -----------------------------------------------------------------------------

print("Path List:\n")

print("using class method:")
for path_list in g.bfsPathList('A', 'F'):
    print("\t", path_list)

print("\n" + "using function:")
for path_list in bfs_path_list(graph_adj_list, 'A', 'F'):
    print("\t", path_list)

# -----------------------------------------------------------------------------
# Shortest Path
# -----------------------------------------------------------------------------

print("\nShortest Path:\n")

print(f"using class method\t: {g.bfsShortestPath('A', 'F')}")
print(f"using function\t\t: {bfs_shortest_path(graph_adj_list, 'A', 'F')}")

# -----------------------------------------------------------------------------
# Output
# -----------------------------------------------------------------------------

# Graph:
#          {'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F'], 'D': ['B'], 'E': ['B', 'F'], 'F': ['C', 'E']} 

# Traversal using Breadth-First Search (BFS):

# using class method      : ['A', 'B', 'C', 'D', 'E', 'F']
# using function          : ['A', 'B', 'C', 'D', 'E', 'F']

# Path List:

# using class method:
#          ['A', 'C', 'F']
#          ['A', 'B', 'E', 'F']

# using function:
#          ['A', 'C', 'F']
#          ['A', 'B', 'E', 'F']

# Shortest Path:
#
# using class method	: ['A', 'C', 'F']
# using function		: ['A', 'C', 'F']
