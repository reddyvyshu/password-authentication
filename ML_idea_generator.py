def generate_ideas():
    ideas = {
        "College": {
            "Problem": "Student performance prediction",
            "Input": "Attendance, assignment scores, study hours",
            "Output": "Predicted grades or pass/fail"
        },
        "Healthcare": {
            "Problem": "Disease prediction",
            "Input": "Symptoms, medical history, test results",
            "Output": "Possible disease or risk level"
        },
        "Shopping": {
            "Problem": "Product recommendation system",
            "Input": "User browsing history, purchase history",
            "Output": "Recommended products"
        }
    }

    for domain, details in ideas.items():
        print("Domain:", domain)
        print("Problem:", details["Problem"])
        print("Input:", details["Input"])
        print("Output:", details["Output"])
        print("-" * 40)

generate_ideas()
