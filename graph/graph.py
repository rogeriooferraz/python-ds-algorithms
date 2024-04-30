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


from ds.linked.queue import CanonicalQueue
from ds.linked.stack import CanonicalStack


class Graph:

    def __init__(self, graph_adj_list = None):
        self.adj_list = {}
        if graph_adj_list:
            for inode, adj_list in graph_adj_list.items():
                self.addVertex(inode)
                for jnode in adj_list:
                    self.addEdge(inode, jnode)

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

    def bfsTraversal(self, origin):
        queue = CanonicalQueue()
        queue.enqueue(origin)
        visited = [origin]
        while queue:
            inode = queue.dequeue()
            for jnode in self.adj_list[inode]:
                if jnode not in visited:
                    queue.enqueue(jnode)
                    visited.append(jnode)
        return visited

    def bfsPathList(self, origin, destination):
        queue = CanonicalQueue()
        queue.enqueue((origin, [origin]))
        while queue:
            (inode, path) = queue.dequeue()
            for jnode in self.adj_list[inode]:
                if jnode not in path:
                    if jnode == destination:
                        yield path + [jnode]
                    else:
                        queue.enqueue((jnode, path + [jnode]))

    def bfsShortestPath(self, origin, destination):
        try:
            return next(self.bfsPathList(origin, destination))
        except StopIteration:
            return None

    def dfsTraversal(self, origin):
        stack = CanonicalStack()
        stack.push(origin)
        visited = []
        while stack:
            inode = stack.pop()
            if(inode not in visited):
                visited.append(inode)
            for jnode in reversed(self.adj_list[inode]):
                if(jnode not in visited):
                    stack.push(jnode)
        return visited

    def dfsPathList(self, origin, destination):
        stack = CanonicalStack()
        stack.push((origin, [origin]))
        while stack:
            (inode, path) = stack.pop()
            for jnode in reversed(self.adj_list[inode]):
                if jnode not in path:
                    if jnode == destination:
                        yield path + [jnode]
                    else:
                        stack.push((jnode, path + [jnode]))
