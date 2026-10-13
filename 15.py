class ExpertSystem:
    def __init__(self):
        self.rules = [
            ({"fever", "cough"}, "Possible Flu", "Get rest and stay hydrated."),
            ({"sore throat", "fever"}, "Possible Throat Infection", "Gargle warm water and consult a doctor."),
            ({"cough", "shortness of breath"}, "Possible Respiratory Issue", "Seek immediate medical attention."),
            ({"runny nose", "sneezing", "sore throat"}, "Possible Common Cold", "Drink warm fluids and rest.")
        ]

    def diagnose(self, user_symptoms):
        return [r for r in self.rules if r[0].issubset(user_symptoms)]

# --- Main Program ---
if __name__ == "__main__":
    print("--- Medical Expert System ---")
    user_input = input("Enter symptoms (comma-separated, e.g., fever, cough): ")
    user_symptoms = {s.strip().lower() for s in user_input.split(",")}
    
    results = ExpertSystem().diagnose(user_symptoms)
    
    print("\nResults:")
    if results:
        for _, diag, rec in results:
            print(f"- {diag}: {rec}")
    else:
        print("No matching conditions found.")