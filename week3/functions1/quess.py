import random
def play_game():
    print("Hello! What is your name?")
    name=input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    number=random.randint(1,20)
    guess = None
    attempts=0
    while guess != number:
        print("Take a guess.")
        guess=int(input())
        attempts+=1
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
    print(f"Good job, {name}! You guessed my number in {attempts} guesses!")

play_game()



