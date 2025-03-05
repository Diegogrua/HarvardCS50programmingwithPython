import random

while True:
    try:
        level = int(input("Level: "))
        n = random.randint(1, level)
        break
    except ValueError:
        print("try again")

while True:
    try:

        guess = int(input("Guess: "))
        if guess < n:
            print("Too small!")
        elif guess > n:
            print("Too large!")
        else:
            print("Just right!")
            break
    except ValueError:
        print("please try again")

print("Gess", n)
