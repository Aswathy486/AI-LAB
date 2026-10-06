def valid(g, r, c, n):
    if n in g[r]:
        return False

    for i in range(9):
        if g[i][c] == n:
            return False

    br, bc = (r//3)*3, (c//3)*3
    for i in range(br, br+3):
        for j in range(bc, bc+3):
            if g[i][j] == n:
                return False
    return True


def solve(g):
    for r in range(9):
        for c in range(9):
            if g[r][c] == 0:
                for n in range(1, 10):
                    if valid(g, r, c, n):
                        g[r][c] = n
                        if solve(g):
                            return True
                        g[r][c] = 0
                return False
    return True


grid = [
[5,3,0,0,7,0,0,0,0],
[6,0,0,1,9,5,0,0,0],
[0,9,8,0,0,0,0,6,0],
[8,0,0,0,6,0,0,0,3],
[4,0,0,8,0,3,0,0,1],
[7,0,0,0,2,0,0,0,6],
[0,6,0,0,0,0,2,8,0],
[0,0,0,4,1,9,0,0,5],
[0,0,0,0,8,0,0,7,9]
]

if solve(grid):
    for row in grid:
        print(row)
else:
    print("No solution")