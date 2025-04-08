from quiz.questions import questions
from quiz.utils import ask_question

def start_quiz():
    print("Welcome to My Python Quiz Game :D!\n")
    score = 0

    for q in questions:
        correct = ask_question(q)
        if correct:
            score += 1
        print() 

    print(f"You got {score} out of {len(questions)} correct.")
