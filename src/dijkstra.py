from collections import deque

INT_MAX = float("inf")

class Graph:
    def __init__(self, filename):
        graph = []
        with open(filename) as f:
            for line in f:
                fr, to, w, *_ = line.strip().split(" ")
                graph.append((fr, to, float(w)))

        self.nodes = set()
        for e in graph:
            self.nodes.update([e[0], e[1]])

        self.adj = {node: set() for node in self.nodes}
        for e in graph:
            self.adj[e[0]].add((e[1], e[2]))

    def search_min(self, dist, visited, start):
        min = INT_MAX
        ret = start
        for node in self.nodes:
            if (visited[node] == False and dist[node] <= min):
                min = dist[node]
                ret = node
        return ret

    def dijkstra(self, start, dest):
        iter = 0
        visited = {}
        dist = {}
        prev = {}
        for node in self.nodes:
            if node == start:
                dist[node] = 0
            else:
                dist[node] = INT_MAX
            prev[node] = None
            visited[node] = False

        for i in range(len(self.nodes) - 1):
            current_node = self.search_min(dist, visited, start)
            visited[current_node] = True
            if dist[current_node] == INT_MAX:
                break
            for adj_node, distance in self.adj[current_node]:
                iter += 1
                if (not visited[adj_node] and dist[current_node] + distance < dist[adj_node]):
                    dist[adj_node] = dist[current_node] + distance
                    prev[adj_node] = current_node
            if current_node == dest:
                break 
        path = deque()
        current_node = dest
        while prev[current_node] is not None:
            path.appendleft(current_node)
            current_node = prev[current_node]
        path.appendleft(start)
        return path, dist[dest], iter