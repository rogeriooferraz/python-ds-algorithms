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

class Stack:

    def __init__(self, data = None):
        self.top = None
        if data:
            self.push(data)

    def push(self, data):
        temp = Node(data)
        temp.next = self.top
        self.top = temp

    def pop(self):      
        if self.top:
            data = self.top.container
            self.top = self.top.next
            return data

    def empty(self):
        return self.top == None

    def __bool__(self):
        return self.empty() == False

    def __str__(self):
        output = ""
        p = self.top 
        while p:
            output += str(p.container) + " "
            p = p.next 
        return output


class Node:
    def __init__(self, data):
        self.container = data
        self.next = None

    def __str__(self):
        return str(self.container)

    def __eq__(self, other):
        return str(self) == str(other)
