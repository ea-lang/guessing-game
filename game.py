play_again = "yes"
while play_again == "yes":   
    import random
    guess_count = 1
    name = raw_input("What is your name?")
    guess = raw_input("%s, I'm thinking of a number between 1 and 100. Try to guess my number." % (name))

    while True:
        try:
           int(guess)
           break
        except ValueError:
            guess = raw_input("Oops, that's not even a number. Try again.")

    guess = int(guess)        
    while guess > 100 or guess < 1:
        guess = raw_input("Wow, silly! That is not a number between 1 and 100! Please try again!")
   

    ranNum = random.randint(1, 100)
    while guess != ranNum:
        if guess > ranNum:
            print("Your guess is too high, try again.")
            guess = int(raw_input("Your guess?"))
            guess_count += 1
        elif guess < ranNum:
            print("Your guess is too low, try again.")
            guess = int(raw_input("Your guess?"))
            guess_count += 1

    print("Well done %s! You found my number in " % (name) + str(guess_count) + " tries!")
    play_again = raw_input("Would you like to start a new game? Yes or No").lower()