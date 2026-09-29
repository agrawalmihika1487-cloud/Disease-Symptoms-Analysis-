
# Disease Analysis Checker
# Educational symptom checker using Python

print("=" * 50)
print("       WELCOME TO DISEASE ANALYSIS CHECKER")
print("=" * 50)

print("\nHello User!")
print("Please answer the following questions with yes or no.")
print("Your answers will be used to analyze your symptoms.\n")

print("IMPORTANT: This program is for educational purposes only.")
print("It does not provide a medical diagnosis.\n")


# Function to accept and validate user answers
def ask_question(question):
    while True:
        answer = input(question + " (yes/no): ").strip().lower()

        if answer == "yes":
            return 1
        elif answer == "no":
            return 0
        else:
            print("Invalid input! Please enter only yes or no.")


# Dictionary to store disease questions
disease_questions = {

    "Dengue": [
        "Do you have a sudden high-grade fever?",
        "Do you feel severe pain behind your eyes?",
        "Do you have severe muscle or joint pain (breakbone fever)?",
        "Have you noticed red pinprick rashes or easy bruising/bleeding?"
    ],

    "Common Cold": [
        "Do you have a runny or congested nose?",
        "Are you sneezing frequently?",
        "Do you have a mild sore throat with little or no fever?"
    ],

    "Hypertension": [
        "Do you get frequent morning headaches at the back of your head?",
        "Do you experience episodes of dizziness, blurry vision, or ringing in the ears?"
    ],

    "Tension Headache": [
        "Does the headache feel like a tight band or heavy pressure around your forehead?",
        "Is the pain mild-to-moderate without any nausea or vomiting?"
    ]
}


# Dictionary to store the scores
scores = {}

# Ask questions for each disease
for disease, questions in disease_questions.items():

    print("\n--- Questions about", disease, "symptoms ---")

    score = 0

    for question in questions:
        score += ask_question(question)

    scores[disease] = score


# Display analysis results
print("\n" + "=" * 50)
print("             DISEASE ANALYSIS REPORT")
print("=" * 50)

print("\nYour symptom response summary:")

for disease, score in scores.items():
    total_questions = len(disease_questions[disease])
    print(f"{disease}: {score}/{total_questions} symptoms reported")


# Find the highest matching score
highest_score = max(scores.values())

matching_diseases = [
    disease
    for disease, score in scores.items()
    if score == highest_score
]


# Display the result
print("\n--- Analysis Result ---")

if highest_score == 0:
    print("No listed symptoms were reported.")

elif len(matching_diseases) == 1:
    print("Your answers most closely match the symptom group:")
    print(matching_diseases[0])

else:
    print("Your answers match multiple symptom groups:")
    for disease in matching_diseases:
        print("-", disease)

print("\nPlease remember:")
print("This result is not a confirmed medical diagnosis.")
print("Symptoms alone cannot confirm a disease.")
print("Consult a qualified healthcare professional for advice.")

print("\nThank you for using Disease Analysis Checker!")