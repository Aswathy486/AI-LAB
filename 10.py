leaf = [5,3,2,4,1,3,6,2,8,7,5,1,3,4]
i = 0
pruned = 0

def ab(d, a, b, ismax):
    global i, pruned

    if d == 0:
        x = leaf[i]
        i += 1
        return x

    if ismax:
        v = float('-inf')
        for _ in range(2):
            v = max(v, ab(d-1,a,b,False))
            a = max(a,v)
            if a >= b:
                pruned += 2**(d-1)
                break
        return v

    else:
        v = float('inf')
        for _ in range(2):
            v = min(v, ab(d-1,a,b,True))
            b = min(b,v)
            if a >= b:
                pruned += 2**(d-1)
                break
        return v

ans = ab(4, float('-inf'), float('inf'), False)

print("MINIMAX value:", ans)
print("Leaf nodes evaluated:", i)
print("Leaf nodes pruned:", pruned)