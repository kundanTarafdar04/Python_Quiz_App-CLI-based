import json
import random

# Load your questions
with open("python_quiz_data.json", "r") as f:
    questions = json.load(f)

random.shuffle(questions)  # Randomize the Order

score = 0
questions_attempted = 0

print("🔥Top Easy 30 Python Questions🔥")
# Printing Questions
for i, q in enumerate(questions, 1):
    print("\n"f"Q{i}. {q['question']}")

    # Printing Options For Each Question
    for opt in q['options']:
        print(opt)

    # Taking Answer From The Users
    ans = input(
        "\nYour Answer:\nA / B / C / D\n(Or press 'Z' to finish) :- ").strip().lower()

    # Comparing The Answer
    if ans == 'z':
        print("\nExiting Quiz....")
        break
    elif ans == q['answer'].lower():
        print("CORRECT ✅")
        score += 1  # Counter For Score
    else:
        print(f"\nWRONG❌, The Answer is {q['answer']}")

    questions_attempted += 1  # Counter For Attempted Questions
print(f"\nYou've Visited [{questions_attempted}/{len(questions)}]")

# Final Score Summary
if score >= 1:
    print(f"\n🎉 Great! Your Score is: [{score}/{len(questions)}]")
else:
    print("Don't Give Up, Just Grind Yourself!!!")
