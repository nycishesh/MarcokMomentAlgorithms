def bfs(visitedBFS, graph, node, queue):
  visitedBFS.append(node)
  queue.append(node)

  while queue:          
    m = queue.pop(0) 
    print (m, end = " ") 

    for neighbour in graph[m]:
      if neighbour not in visitedBFS:
        visitedBFS.append(neighbour)
        queue.append(neighbour)
