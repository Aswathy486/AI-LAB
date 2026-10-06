import heapq
graph = {
    'A':[('B',1),('C',3)],
    'B':[('D',3),('E',1)],
    'C':[('F',5)],
    'D':[('G',2)],
    'E':[('G',4)],
    'F':[('G',1)],
    'G':[]
}
h = {'A':5,'B':4,'C':4,'D':2,'E':2,'F':1,'G':0}
def astar(start, goal):
    pq = [(0, start)]
    g = {start:0}
    parent = {start:None}
    while pq:
        f, cur = heapq.heappop(pq)
        if cur == goal:
            path = []
            while cur:
                path.append(cur)
                cur = parent[cur]
            return path[::-1], g[goal]
        for nxt, cost in graph[cur]:
            ng = g[cur] + cost
            if nxt not in g or ng < g[nxt]:
                g[nxt] = ng
                parent[nxt] = cur
                heapq.heappush(pq, (ng + h[nxt], nxt))
path, cost = astar('A', 'G')
print("Shortest Path:", " -> ".join(path))
print("Total Cost:", cost)