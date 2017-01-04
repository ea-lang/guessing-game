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
score_list = []

while play_again == "yes":   
    import random
    guess_count = 1
    name = raw_input("What is your name?")
    guess = int(goodNumber(raw_input("%s, I'm thinking of a number between 1 and 100. Try to guess my number." % (name))))
    ranNum = random.randint(1, 99)

    while guess != ranNum:
        if guess > ranNum:
            print("Your guess is too high, try again.")
            guess = int(goodNumber(raw_input("Your guess?")))
            guess_count += 1
        elif guess < ranNum:
            print("Your guess is too low, try again.")
            guess = int(goodNumber(raw_input("Your guess?")))
            guess_count += 1
    score_list.append(guess_count)
    best_score = min(score_list)
    print "Well done %s! You found my number in %d tries! The best score is %d!" % (name, guess_count, best_score)
    play_again = raw_input("Would you like to start a new game? Yes or No").lower()
    


