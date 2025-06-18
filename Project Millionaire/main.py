# Create some questions in list
questions = [
    {
        "question": "Who is known as the 'Megastar' of Telugu cinema?",
        "options": ["Nagarjuna", "Chiranjeevi", "Venkatesh", "Mahesh Babu"],
        "answer": "Chiranjeevi"
    },
    {
        "question": "Which film is considered the first Telugu talkie?",
        "options": ["Malliswari", "Bhakta Prahlada", "Mayabazar", "Pathala Bhairavi"],
        "answer": "Bhakta Prahlada"
    },
    {
        "question": "Who directed the blockbuster movie 'Baahubali'?",
        "options": ["Trivikram Srinivas", "S. S. Rajamouli", "Puri Jagannadh", "Koratala Siva"],
        "answer": "S. S. Rajamouli"
    },
    {
        "question": "Which actress is popularly known as the 'Lady Superstar' of Telugu cinema?",
        "options": ["Anushka Shetty", "Samantha Ruth Prabhu", "Kajal Aggarwal", "Tamannaah Bhatia"],
        "answer": "Anushka Shetty"
    },
    {
        "question": "Which Telugu film won the National Film Award for Best Feature Film in 2017?",
        "options": ["Baahubali 2: The Conclusion", "Ghazi", "Arjun Reddy", "Mahanati"],
        "answer": "Baahubali 2: The Conclusion"
    },
    {
        "question": "Who is yeti in devara movie?",
        "options": ["Srikanth", "Saif ali khan", "NTR", "Prakesh Raj"],
        "answer": "Prakesh Raj"
    }

]


def play_game(questions):
    score = 0
    for i, q in enumerate(questions):
        print(f"Question {i + 1}: {q['question']}")
        for j, option in enumerate(q['options']):
            print(f"{j + 1}. {option}")

        answer = input("Your answer (1-4): ")

        if q['options'][int(answer) - 1] == q['answer']:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {q['answer']}\n")

    print(f"Your final score is: {score}/{len(questions)}")
    print("The Cash prize you won is: ", end="")
    if score == len(questions):
        print("₹ 1,000,000")
    elif score >= len(questions) // 2:
        print("₹ 50,000")
    else:
        print("₹ 1,000")



def start_game():
    print("\nThis game is designed by @Akhil-28407\n\n")
    print("          Telugu Cinema Quiz            ")
    print("========================================\n")
    print("Welcome to the Telugu Cinema Quiz!")
    print("You will be asked a series of questions about Telugu cinema.")
    print("Choose the correct answer by entering the number corresponding to your choice.")
    print("Let's begin!\n")

    play_game(questions)


start_game()
