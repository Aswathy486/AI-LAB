import random
def simple_hill(x, n):
    for i in n:
        if i > x:
            return i
    return x

def steepest_hill(x, n):
    best = max(n)
    return best if best > x else x

def stochastic_hill(x, n):
    better = [i for i in n if i > x]
    return random.choice(better) if better else x

x = int(input("Enter current value: "))
n = list(map(int, input("Enter neighbors separated by space: ").split()))

print("\nCurrent:", x)
print("Neighbors:", n)
print("Simple Hill Climbing:", simple_hill(x, n))
print("Steepest-Ascent Hill Climbing:", steepest_hill(x, n))
print("Stochastic Hill Climbing:", stochastic_hill(x, n))