from queue import PriorityQueue
import networkx as nx

def dijkstra(graph: 'nx.classes.graph.Graph', start: str, end: str):
    def cost(u, v):
        return graph.get_edge_data(u, v).get('grade')
        
    prev = {}
    dist = {v: float('inf') for v in list(nx.nodes(graph))}
    visited = set()
    pq = PriorityQueue()
    
    dist[start] = 0
    pq.put((dist[start], start))
    
    while not pq.empty():
        curr_cost, curr = pq.get()
        visited.add(curr)
        print(f'visiting {curr}')
        for neighbor in dict(graph.adjacency()).get(curr):
            path = dist[curr] + cost(curr, neighbor)
            if path < dist[neighbor]:
                dist[neighbor] = path
                prev[neighbor] = curr
                if neighbor not in visited:
                    visited.add(neighbor)
                    pq.put((dist[neighbor], neighbor))
                else:
                    pq.get((dist[neighbor], neighbor))
                    pq.put((dist[neighbor], neighbor))
