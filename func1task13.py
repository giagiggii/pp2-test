import random
def guess_the_number():
    secret_number = random.randint(1, 20)
    #nachinaem
    print("Hello! What is your name?")
    s=input()

    print("Well,", s ,",I am thinking of a number between 1 and 20.Take a guess.")

    guesses = 0

    while True:
        guess = int(input())
        guesses += 1

        if guess == secret_number:
            print(f"Good job,",s, "You guessed my number in", {guesses} ,"guesses!")
            break
        elif guess < secret_number:
            print("Your guess is too low. Take a guess")
        else:
            print("Your guess is too high. Take a guess")

guess_the_number()
