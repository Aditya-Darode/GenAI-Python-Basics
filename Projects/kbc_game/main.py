# List of questions with options and correct answer index
# Format: [Question, Option A, Option B, Option C, Option D, Correct Option Number]
questions = [
    ["1. Who is Shah Ruk Khan?", "WWE Wrestler", "Actor", "Comman Man", "Astronaut", 2],
    ["2. What is the capital of France?", "Berlin", "Paris", "Rome", "London", 2],
    ["3. Which planet is known as the red planet?", "Earth", "Jupiter", "Venus", "Mars", 4],
    ["4. Which is the largest animal?", "Whale", "Shark", "Elephant", "Giraffe", 1],
    ["5. Who wrote Romeo and Juliet?", "William Shakespeare", "Jane Austen", "Charles Dickens", "Homer", 1],
    ["6. How many players are there in a cricket team?", "9", "10", "11", "12", 3],
    ["7. Which is the longest river in the world?", "Amazon", "Nile", "Ganga", "Yangtze", 2],
    ["8. Who discovered gravity?", "Albert Einstein", "Galileo Galilei", "Isaac Newton", "Charles Darwin", 3],
    ["9. Which organ purifies blood in the human body?", "Heart", "Lungs", "Kidney", "Liver", 3],
    ["10. What was the name of Arjuna's bow?", "Gandiva", "Pinaka", "Sharanga", "Vijaya", 1],
]

# Prize money for each correct answer
prizes = ["₹1,000", "₹2,000", "₹3,000", "₹5,000", "₹10,000", "₹20,000", "₹40,000", "₹80,000", "₹1,60,000", "₹3,20,000"]

i = 0  # Keeps track of the current question index

# Loop through each question
for question in questions:
    # Display the question and its options
    print(question[0])
    print(f"A. {question[1]}")
    print(f"B. {question[2]}")
    print(f"C. {question[3]}")
    print(f"D. {question[4]}")

    # Take user input for answer
    a = int(input("Enter your answer: 1 for A, 2 for B, 3 for C, 4 for D\n"))

    # Check if the answer is correct
    if question[5] == a:
        print("✅ Correct Answer")
    else:
        print(f"❌ Incorrect, the correct answer was {question[5]}")
        print("Better luck next time!")
        break  # End the game if answer is wrong

    # Display the prize won
    print(f"You Won {prizes[i]}")
    i += 1
