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


from graph import Graph


def dfs_traversal(adj_list, orig_node):
    visited = []
    stack = [orig_node]
    while stack:
        inode = stack.pop()
        if(inode not in visited):
            visited.append(inode)
        for jnode in reversed([ adj_v for adj_v in adj_list[inode] if adj_v not in visited ]):
            stack.append(jnode)
    return visited


def dfs_path_list(adj_list, orig_vertex, dest_vertex):
    stack = [(orig_vertex, [orig_vertex])]
    while stack:
        (inode, path) = stack.pop()
        for jnode in reversed([ adj_v for adj_v in adj_list[inode] if adj_v not in path ]):
            if jnode == dest_vertex:
                yield path + [jnode]
            else:
                stack.append((jnode, path + [jnode]))


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
print(f"\t{g}\n")

# -----------------------------------------------------------------------------
# Traversal using Depth-First Search (DFS)
# -----------------------------------------------------------------------------

print("Traversal using Depth-First Search (DFS):\n")

print(f"using class method\t: {g.dfsTraversal('A')}")
print(f"using function\t\t: {dfs_traversal(graph_adj_list, 'A')}\n")

# -----------------------------------------------------------------------------
# Path List
# -----------------------------------------------------------------------------

print("Path List:\n")

print("using class method:")
for path_list in g.dfsPathList('A', 'F'):
    print(f"\t{path_list}")

print("\n" + "using function:")
for path_list in dfs_path_list(graph_adj_list, 'A', 'F'):
    print(f"\t{path_list}")

# -----------------------------------------------------------------------------
# Output
# -----------------------------------------------------------------------------

# Graph:
#     {'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F'], 'D': ['B'], 'E': ['B', 'F'], 'F': ['C', 'E']}

# Traversal using Depth-First Search (DFS):

# using class method    : ['A', 'B', 'D', 'E', 'F', 'C']
# using function        : ['A', 'B', 'D', 'E', 'F', 'C']

# Path List:

# using class method:
#     ['A', 'B', 'E', 'F']
#     ['A', 'C', 'F']

# using function:
#     ['A', 'B', 'E', 'F']
#     ['A', 'C', 'F']
