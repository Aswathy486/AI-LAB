def forward(facts, rules):
    print("Initial Facts:", facts)
    while True:
        new = False
        for c, r in rules:
            if c in facts and r not in facts:
                facts.append(r)
                print("Rule applied:", c, "->", r)
                print("New fact:", r)
                new = True
        if not new:
            break
    return facts
facts = ["It is raining"]
rules = [
    ("It is raining", "The ground is wet"),
    ("The ground is wet", "The road is slippery")
]
result = forward(facts, rules)
print("\nFinal Set of Facts:")
for x in result:
    print("-", x)