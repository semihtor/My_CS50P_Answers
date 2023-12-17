import random

while True:
    try:
        level = int(input("Level: "))
        if level >= 1:
            break
    except:
        # ask again if float, negative or regular string
        pass

number_to_be_guessed = random.randint(1, level)

while True:
    try:
        users_guess = int(input("Guess: "))
        if users_guess >= 1:
            if users_guess < number_to_be_guessed:
                print("Too small!")
            elif number_to_be_guessed < users_guess:
                print("Too large!")
            else:
                print("Just right!")
                break

    except:
        pass
