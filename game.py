def stringChecker(string):
    try:
        int(string)
        return True
    except ValueError:
        return False

def rangeChecker(num):
    num = int(num)
    if num < 100 and num > 1:
        return True
    else:
        return False

def goodNumber(num):
    while True:
        if stringChecker(num) == True and rangeChecker(num) == True:
            return num
        else:
            num = raw_input("That is an invalid entry, please try again.")
            continue 

play_again = "yes"
scoreList = []

while play_again == "yes":   
    import random
    guess_count = 1
    name = raw_input("What is your name?")
    guess = int(goodNumber(raw_input("%s, I'm thinking of a number between 1 and 100. Try to guess my number." % (name))))
    while guess > 100 or guess < 1:
        guess = int(goodNumber(raw_input("Wow, silly! That is not a number between 1 and 100! Please try again!")))
   

    ranNum = random.randint(1, 100)

    while guess != ranNum:
        if guess > ranNum:
            print("Your guess is too high, try again.")
            guess = int(goodNumber(raw_input("Your guess?")))
            guess_count += 1
        elif guess < ranNum:
            print("Your guess is too low, try again.")
            guess = int(goodNumber(raw_input("Your guess?")))

            guess_count += 1
    scoreList.append(guess_count)
    best_score = min(scoreList)
    print("Well done %s! You found my number in " % (name) + str(guess_count) + " tries! The best score is " + str(best_score) + "!")
    play_again = raw_input("Would you like to start a new game? Yes or No").lower()
    


