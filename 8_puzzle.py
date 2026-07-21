from collections import deque

goal = ((1,2,3),(4,5,6),(7,8,0))

def neighbors(s):
    x,y = [(i,j) for i in range(3) for j in range(3) if s[i][j]==0][0]
    n = []
    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        nx,ny = x+dx,y+dy
        if 0<=nx<3 and 0<=ny<3:
            t = [list(r) for r in s]
            t[x][y],t[nx][ny] = t[nx][ny],t[x][y]
            n.append(tuple(map(tuple,t)))
    return n

def bfs(start):
    q = deque([start])
    parent = {start:None}

    while q:
        cur = q.popleft()
        if cur == goal:
            path = []
            while cur:
                path.append(cur)
                cur = parent[cur]
            for state in path[::-1]:
                for row in state:
                    print(row)
                print()
            return

        for nxt in neighbors(cur):
            if nxt not in parent:
                parent[nxt] = cur
                q.append(nxt)

start = ((1,2,3),(4,0,6),(7,5,8))
bfs(start)