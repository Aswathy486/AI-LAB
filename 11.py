# Experiment 11: Knowledge Representation

facts = [
    {"subject": "Dog", "relation": "is_a", "object": "Animal"},
    {"subject": "Dog", "relation": "has", "object": "Fur"},
    {"subject": "Animal", "relation": "needs", "object": "Food"}
]

rules = [
    {
        "if": {"subject": "Dog", "relation": "is_a", "object": "Animal"},
        "then": {"subject": "Animal", "relation": "can", "object": "Breathe"}
    },
    {
        "if": {"subject": "Dog", "relation": "has", "object": "Fur"},
        "then": {"subject": "Dog", "relation": "is", "object": "Mammal"}
    }
]

print("--- Initial Knowledge Base ---")
for fact in facts:
    print(f"{fact['subject']} -> {fact['relation']} -> {fact['object']}")

derived_facts = []

for rule in rules:
    if rule["if"] in facts:
        conclusion = rule["then"]
        if conclusion not in facts:
            facts.append(conclusion)
            derived_facts.append(conclusion)

print("\n--- Derived Knowledge ---")
for fact in derived_facts:
    print(f"{fact['subject']} -> {fact['relation']} -> {fact['object']}")

print("\n--- Final Knowledge Base ---")
for fact in facts:
    print(f"{fact['subject']} -> {fact['relation']} -> {fact['object']}")