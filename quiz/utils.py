def ask_question(q):
    print(q["question"])
    for idx, opt in enumerate(q["options"], start=1):
        print(f"{idx}. {opt}")

    try:
        choice = int(input("Enter your choice (1-4): "))
        if q["options"][choice - 1] == q["answer"]:
            print("Correct!")
            return True
        else:
            print(f"Wrong! The answer was: {q['answer']}")
            return False
    except (ValueError, IndexError):
        print("Invalid input! Please choose a number between 1-4.")
        return False
