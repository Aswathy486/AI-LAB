flights = {"F1": 8, "F2": 9, "F3": 11, "F4": 12}
aircraft = ["A1", "A2"]
crew = ["C1", "C2", "C3"]
slots = [8, 9, 10, 11, 12]

schedule = {}

def solve(i=0):
    if i == len(flights):
        return True

    f = list(flights)[i]
    for t in slots:
        for a in aircraft:
            for c in crew:
                if t == flights[f] and t not in [x[2] for x in schedule.values()]:
                    if a not in [x[0] for x in schedule.values()] or \
                       c not in [x[1] for x in schedule.values()]:
                        schedule[f] = (a, c, t)
                        if solve(i + 1):
                            return True
                        del schedule[f]
    return False

if solve():
    print("Flight\tAircraft Crew\tTime")
    for f, x in schedule.items():
        print(f,"\t",x[0],"\t", x[1],"\t", x[2])
else:
    print("No valid schedule")