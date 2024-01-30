title = "Kaun Banega Crorepati"
rewards = ("Rs.1000", "Rs.2000", "Rs.3000", "Rs.5000", "Rs.10,000 <safe level>", "Rs.20,000", "Rs.40,000", "Rs.80,000", "Rs.1,60,000", "Rs.3,20,000 <safe level>", "Rs.6,25,000", "Rs.12,50,000", "Rs.25,00,000", "Rs.50,00,000", "Rs.1,00,00,000 <grand reward>")

questions = (
    "1. What is the most popular programming language in the world?",
    "2. What does 'CPU'' stand for?",
    "3. What is the binary equivalent of the decimal number 10?",
    "4. What is the name of the operating system used on most Apple computers?",
    "5. What is the purpose of a firewall?",
    "6. What is the difference between a compiler and an interpreter?",
    "7. What is the name of the algorithm used to search for information on the internet developed by Google?",
    "8. What is the difference between RAM and ROM?",
    "9. What is the purpose of a blockchain?",
    "10. What is the name of the artificial intelligence program that defeated the world champion at Go in 2016?",
    "11. What is the fundamental theoretical limitation of any classical computer, as proven by Gödel's incompleteness theorems?",
    "12. Which of the following is a cryptographic hash function often used for digital signatures and file integrity verification?",
    "13. In the context of cryptography, what property allows public-key encryption to work securely?",
    "14. What is the difference between quantum computing and traditional computing?",
    "15. What is the Turing Test?"
)

options = (
    ("a] Python", "b] Java", "c] C++", "d] Javascript"),
    ("a] Computer Peripherals Unit", "b] Central Processing Unit", "c] Code Publishing Utility", "d] Central Program Utility"),
    ("a] 01", "b] 1101", "c] 10", "d] 1010"),
    ("a] macOS", "b] Windows", "c] iOS", "d] Android"),
    ("a] To create new files", "b] To run virtual machines", "c] To protect a computer from unauthorized access", "d] To access websites"),
    ("a] Only a compiler can debug code.", "b] They both do the same thing.", "c] An interpreter creates code while a compiler runs it", "d] A compiler creates code while an interpreter runs it."),
    ("a] Binary search", "b] PageRank", "c] Breadth-first search", "d] Depth-first search"),
    ("a] RAM is volatile, while ROM is non-volatile.", "b] ROM is faster than RAM.", "c] RAM is used for storage, while ROM is used for processing", "d] There is no difference."),
    ("a] To run virtual machines", "b] To protect against malware", "c] To store and transfer data securely", "d] To manage computer networks"),
    ("a] Watson", "b] AlphaGo", "c] Siri", "d] Alexa"),
    ("a] It cannot prove its own consistency.", "b] It cannot solve all NP-complete problems efficiently.", "c] It cannot perfectly simulate quantum mechanics.", "d] It is susceptible to the halting problem."),
    ("a] RES", "b] AES", "c] MD5", "d] SHA-256"),
    ("a] The one-way function property", "b] The private key is kept secret", "c] The message is transmitted through a secure channel", "d] Both the sender and receiver have access to a trusted third party"),
    ("a] Quantum computers use qubits, while traditional computers use bits.", "b] Quantum computers are faster than traditional computers for all tasks", "c] Quantum computers are only useful for cryptography.", "d] There is no difference."),
    ("a] A test to measure the speed of a computer.", "b] A test to measure the intelligence of a computer program.", "c] A test to measure the security of a computer system.", "d] A test to measure the usability of a computer interface.")
)

answers = ("a", "b", "d", "a", "c", "d", "b", "a", "c", "b", "a", "d", "b", "a", "b")

valid_input = ("a", "b", "c", "d", "q")

rules = '''
Welcome to the game! Here are the rules and reward system:

General Rules:

- You'll answer 15 questions, each with a corresponding reward [Reward].
- The difficulty increases with each question.
- Answer correctly to progress and win higher rewards.
- Answer incorrectly, and your reward falls back to the previous safe level [Fallback Reward].
- You can quit at any time by typing "q" to secure your current reward [Current Reward].
- Input your answers as a, b, c, or d.
- Lifelines are currently disabled, but you can use Google for assistance.
- There's no time limit per question, so take your time and think carefully.

Reward System:

1.  Rs.1000
2.  Rs.2000
3.  Rs.3000
4.  Rs.5000
5.  Rs.10,000       <safe level>
6.  Rs.20,000
7.  Rs.40,000
8.  Rs.80,000
9.  Rs.1,60,000
10. Rs.3,20,000     <safe level>
11. Rs.6,25,000
12. Rs.12,50,000
13. Rs.25,00,000
14. Rs.50,00,000
15. Rs.1,00,00,000  <grand reward>

Ready to play? Let's get started!
'''

def is_correct_input(user_answer):
    """
    Verifies if user input is correct or not.
    """
    is_correct = False
    while not is_correct:
        if user_answer in valid_input:
            return user_answer
        else:
            user_answer = input("Incorrect choice, try again :(\nYour answer: ").lower()

def is_quitting(user_answer):
    """
    Verifies if user wants to quit the quiz.
    """
    return user_answer == "q"

def fallback_reward(current_index):
    """
    Calculates fallback reward if the user enters an incorrect answer.
    """
    if current_index == 0:
        return "Rs. 0"
    elif 1 <= current_index < 5:
        return rewards[current_index - 1]
    elif 5 <= current_index < 10:
        return "Rs. 10,000"
    else:
        return "Rs. 3,20,000"

def final_reward(current_index, is_quit=False, is_lost=False):
    """
    Calculates final reward if user wins, loses, or quits.
    """
    if is_quit:
        print(f"\nThat was a safe move {user_name}, so you've won { 'Rs.0' if current_index == 0 else rewards[current_index - 1]}")
        print(f"Give it a try again next time {user_name} :)")
    elif is_lost:
        print(f"\nFinal Reward: {fallback_reward(current_index)}")
        print(f"You have given your best, give it a try again next time {user_name} :)")
    else:
        print(f"\nFinal Grand Reward: {(rewards[-1]).replace('<grand reward>', '')}")
        print(f"Adbhut! 1 crore!!!!!!!\nYou have proved that you are worth your dreams!\n\nAuf Wiedersehen {user_name} :)")

print()
print(title.center(70, "_"))
print("\nWelcome to KBC!\nIt's time to show what you got :)")
user_name = input("Please enter your name: ")
print(f"\nHello, {user_name}! Are you familiar with the rules?")

is_rules = False
while not is_rules:
    is_rules = input("Enter y/n: ")
    if is_rules == "y":
        input("\nAlright, press any key to start the quiz...")
        break
    elif is_rules == "n":
        print(rules)
        input("\nPress any key to start the quiz...")
        break
    else:
        print("Try again :(")
        is_rules = False

for question in questions:
    current_index = questions.index(question)

    print("\n".ljust(50, "-"))
    print(f"Reward: {rewards[current_index]}")
    print(f"Current Reward: { 'Rs.0' if current_index == 0 else rewards[current_index - 1]}")
    print(f"Fallback Reward: {fallback_reward(current_index)}")
    print(question)

    loop_index = 0
    for option in options:
        if loop_index == current_index:
            for opt in option:
                print(opt)
        loop_index += 1

    user_answer = is_correct_input(input("Your answer: ").lower())

    if is_quitting(user_answer):
        final_reward(current_index, True)
        break

    correct_answer = answers[current_index]

    if user_answer == correct_answer and current_index == len(rewards) - 1:
        final_reward(current_index)
    elif user_answer == correct_answer:
        print(f"Correct!\tHere's the next question for {rewards[current_index + 1]}")
    else:
        print("Oops, that was incorrect :(")
        final_reward(current_index, False, True)
        break

input("\nPress any key to exit ¯\_(ツ)_/¯\n")
