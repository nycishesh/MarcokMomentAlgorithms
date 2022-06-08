visitedDFS = set()
def dfs(visitedDFS, graph, node):
    if node not in visitedDFS:
        print (node)
        visitedDFS.add(node)
        for neighbour in graph[node]:
            dfs(visitedDFS, graph, neighbour)
