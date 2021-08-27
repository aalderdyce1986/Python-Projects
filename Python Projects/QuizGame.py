#---------------------- Quiz Game -------------------------------------------
def newGame():
    guesses = []
    correctGuesses = 0
    qstNum = 1

    for key in questions:
        print("--------------------------------")
        print(key)
        for i in options[qstNum-1]:
            print(i)
        guess = input("Enter (A, B, C or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correctGuesses += checkAnswer(questions.get(key), guess)
        qstNum += 1

    displayScore(correctGuesses, guesses)
#--------------------------------
def checkAnswer(answer, guess):
    if answer == guess:
        print("CORRECT!!")
        return 1
    else:
        print("WRONG!!")
        return 0
#--------------------------------
def displayScore(correctGuesses, guesses):
    print("--------------------------------")
    print("RESULTS: ")
    print("--------------------------------")
    print("Answers: ", end =" ")
    for i in questions:
        print(questions.get(i), end = " ")
    print()
    
    print("Guesses: ", end =" ")
    for i in guesses:
        print(i, end = " ")
    print()

    score = ((correctGuesses/len(questions))*100)
    print("Your score is: " + str(score) + "%")
#--------------------------------
def playAgain():
    response = input("Would you like to play again? (yes or no)")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False
#--------------------------------

questions = {
    "Who created Python?" : "A",
    "What year was Python created?: ": "B",
    "Python is tributed to which comedy group?: ": "C",
    "Is the Earth round?:" : "A"
    }

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
            ["A. 1989", "B. 1981", "C. 2000", "D. 2016"], 
            ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
            ["A. True", "B. False", "C. Sometimes", "D. What's Earth?"]]

newGame()

while playAgain():
    newGame()
print("So long, see you next time!")
 
