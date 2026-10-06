# Experiment 12: Travelling Salesman Problem using Hill Climbing

cities = ['A', 'B', 'C', 'D']

dist = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

def cost(tour):
    return sum(dist[tour[i]][tour[(i + 1) % len(tour)]]
               for i in range(len(tour)))

def hill_climb(tour):
    while True:
        best = tour
        best_cost = cost(tour)

        for i in range(1, len(tour) - 1):
            for j in range(i + 1, len(tour)):
                new = tour[:]
                new[i], new[j] = new[j], new[i]

                if cost(new) < best_cost:
                    best, best_cost = new, cost(new)

        if best == tour:
            return tour
        tour = best

tour = [0, 1, 2, 3]
result = hill_climb(tour)

print("Final Tour:", " -> ".join(cities[i] for i in result), "->", cities[result[0]])
print("Total Distance:", cost(result))