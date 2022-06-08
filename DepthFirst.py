def dfs(visitedDFS: set(), graph, node):
    if node not in visitedDFS:
        print (node)
        visitedDFS.add(node)
        for neighbour in graph[node]:
            dfs(visitedDFS, graph, neighbour)
    
    return 