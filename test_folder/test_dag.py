
'''

Directed acyclic graph

In mathematics, particularly graph theory, and computer science,
a directed acyclic graph is a directed graph with no directed cycles.

That is, it consists of vertices and edges,
with each edge directed from one vertex to another,
such that following those directions will never form a closed loop.

useful links:
    https://en.wikipedia.org/wiki/Directed_acyclic_graph
    https://github.com/networkx/networkx

what is a stack:
    https://www.educative.io/edpresso/how-to-implement-stack-in-python

'''

# the graph is best represented in the hash (a python dict)
graph = {
    'a': ['b','c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e':[],
    'f':[]
    }



def traverse_graph(graph ,source):

    stack = [source]
    
    while (len(stack)>0 ):
        current = stack.pop()
        print(current)
    
        for neighbour in graph[current]:
            stack.append(neighbour)
    return


traverse_graph(graph, 'a')

