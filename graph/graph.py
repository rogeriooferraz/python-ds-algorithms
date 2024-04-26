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

from ds.linked.queue import Queue
from ds.linked.stack import Stack


class Graph:

    def __init__(self, graph_adj_list = None):
        self.adj_list = {}
        if graph_adj_list:
            for vertex in graph_adj_list:
                self.addVertex(vertex)
                for adj_vertex in graph_adj_list[vertex]:
                    self.addEdge(vertex, adj_vertex)

    def __str__(self):
        return str(self.adj_list)

    def addEdge(self, vertex, adj_vertex):
        try:
            self.adj_list[vertex].append(adj_vertex)
        except:
            print(f"Error: vertex {vertex} is not defined")

    def addVertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def bfsTraversal(self, orig_node):
        queue = Queue(orig_node)
        visited = [orig_node]
        while queue:
            inode = queue.dequeue()
            for jnode in self.adj_list[inode]:
                if jnode not in visited:
                    queue.enqueue(jnode)
                    visited.append(jnode)
        return visited

    def bfsPathList(self, orig_vertex, dest_vertex):
        queue = Queue((orig_vertex, [orig_vertex]))
        while queue:
            (inode, path) = queue.dequeue()
            for jnode in self.adj_list[inode]:
                if jnode not in path:
                    if jnode == dest_vertex:
                        yield path + [jnode]
                    else:
                        queue.enqueue((jnode, path + [jnode]))

    def bfsShortestPath(self, orig_vertex, dest_vertex):
        try:
            return next(self.bfsPathList(orig_vertex, dest_vertex))
        except StopIteration:
            return None

    def dfsTraversal(self, orig_node):
        stack = Stack(orig_node)
        visited = []
        while stack:
            inode = stack.pop()
            if(inode not in visited):
                visited.append(inode)
            for jnode in reversed(self.adj_list[inode]):
                if(jnode not in visited):
                    stack.push(jnode)
        return visited

    def dfsPathList(self, orig_vertex, dest_vertex):
        stack = Stack((orig_vertex, [orig_vertex]))
        while stack:
            (inode, path) = stack.pop()
            for jnode in self.adj_list[inode]:
                if jnode not in path:
                    if jnode == dest_vertex:
                        yield path + [jnode]
                    else:
                        stack.push((jnode, path + [jnode]))
