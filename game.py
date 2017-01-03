import random

# Put your code here
guess_count = 1
name = raw_input("What is your name?")
guess = int(raw_input("%s, I'm thinking of a number between 1 and 100. Try to guess my number." % (name)))
ranNum = random.randint(1, 100)
if type(guess) != 'int' or guess > 100 or guess < 100:
    guess = int(raw_input("Wow, silly, that is not a number between 1 and 100! Please try again."))
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
