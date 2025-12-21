#-----------------------------
def new_game():

    guesses=[]
    correct_guesses=0
    question_number=1

    for key in questions:
        print("*************************************")
        print(key)
        for i in options[question_number-1]:
            print(i)
        guess=input("Enter your guess(A,B,C,D): ")
        guess=guess.upper()
        guesses.append(guess)
        correct_guesses += check_answers (questions.get(key),guess)
        question_number+=1

    score(correct_guesses , guesses)

#-----------------------------
def check_answers(answers,guess):
    if answers==guess:
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        return 0
#-----------------------------
def score(correct_guesses , guesses):
    print("-----------------------------------")
    print("RESULTS")
    print("----------------------------------")
    print("answers:",end="")
    for i in questions:
        print(questions.get(i),end="")
    print()
    print("guesses:", end="")
    for i in guesses:
        print(i, end="")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("your score is :"+str(score)+"%")

#-----------------------------
def play_again():
    response=input("Do you want to play again?(Yes/No): ")
    response=response.upper()
    if response=="YES":
        return True
    else:
        return False
#-----------------------------


questions={"Who created Python:":"A",
           "What year was Python invented: ":"B",
           "choose the odd one out:":"C",
           "what is the full form of OOPS:":"A",
           "choose the correct integer datatype":"D"
           }
options=[["A. Guido Van Rossum","B. Elon Musk ","C. Bill Gates","D. Mark Zuckerberg" ],
         ["A. 1989","B. 1991","c. 2000","D. 2016"],
         ["A. variables","B. Keyword","C. book","D. dictionary "],
         ["A. Object Oriented Programming Language","B. Object Oracle Programming Language","C. Object Orange Papaya Lemon","D. Object oriented python language"],
         ["A. %c","B. %i","C. %f","D. %d"]]
new_game()

while play_again():
    new_game()
print("GAME OVER")