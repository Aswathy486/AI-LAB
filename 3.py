import math
def minimax(d, i, m, a, b):
    if d == h:
        return v[i]
    if m:
        x = -math.inf
        for k in range(2):
            x = max(x, minimax(d+1, i*2+k, 0, a, b))
            a = max(a, x)
            if a >= b: break
    else:
        x = math.inf 
        for k in range(2):
            x = min(x, minimax(d+1, i*2+k, 1, a, b))
            b = min(b, x)
            if a >= b: break
    return x
h = int(input("Enter depth of tree: "))
v = list(map(int, input(f"Enter {2**h} leaf node values: ").split()))
print("Optimal Value =", minimax(0, 0, 1, -math.inf, math.inf))