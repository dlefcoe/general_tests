




def has_path_depth(graph, src, dst):
    ''' function to determine if the graph has a path
    from the source (src) to the destination (dst).
    '''

    if (src==dst):
        return True
    
    for neighbour in graph[src]:
        if(has_path_depth(graph, neighbour, dst)==True):
            return True


    return False


def has_path_breadth(graph, src, dst):
    ''' function to determine if the graph has a path
    from the source (src) to the destination (dst).
    ''' 
    queue = [src]

    while(len(queue)>0):
        current = queue.pop(0)

        if current==dst: return True
        for neighbour in graph[current]:
            queue.append(neighbour)        

    return False



graph = {
    'f':['g','i'],
    'g':['h'],
    'h':[],
    'i':['g', 'k'],
    'k':[]
}


if __name__ == '__main__':
    x=has_path_depth(graph, 'f', 'k')
    y=has_path_breadth(graph, 'f', 'k')
    print(x, y)
