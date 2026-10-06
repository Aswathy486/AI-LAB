classes = {
    "ANN": (["S3","S5"],40), "TOC": (["S3"],45),
    "AGA": (["S5"],40), "ML": (["S3"],45),
    "CN": (["S5"],40)
}

slots = ["P1 9:00-9:55","P2 9:55-10:50","P3 11:05-11:55",
         "P4 11:55-12:45","P5 1:35-2:30","P6 2:30-3:25",
         "P7 3:40-4:30","P8 4:30-5:30"]

rooms = {"208": 60, "305": 60}
schedule = {}

def valid(c, t, r):
    if classes[c][1] > rooms[r]: return False
    for x,(xt,xr) in schedule.items():
        if t == xt and (r == xr or
           set(classes[c][0]) & set(classes[x][0])): return False
    return True

def solve(i=0):
    names = list(classes)
    if i == len(names): return True
    c = names[i]
    for t in slots:
        for r in rooms:
            if valid(c,t,r):
                schedule[c] = (t,r)
                if solve(i+1): return True
                del schedule[c]
    return False

solve()

print("Class\t\tTime\t\t\tRoom")
print("-"*35)
for c,(t,r) in schedule.items():
    print(f"{c}\t\t{t}\t\t{r}")