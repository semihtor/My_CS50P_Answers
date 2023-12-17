import random


def main():
    level = get_level()
    print(start_game(level))


def get_level():

    while True:
        try:
            level = int(input("Level: "))
            if 3 >= level >= 1:
                break
        except:
            # ask again if not 1, 2 or 3
            pass
    return level


def generate_integer(level):
    if level == 1:
        # changed because pow(10, 0) equals 1, not 0
        range_start = 0
    else:
        range_start = 10**(level-1)
    range_end = (10**level)-1
    x = random.randint(range_start, range_end)
    y = random.randint(range_start, range_end)
    return x, y


def create_problem(x, y):
    user_tries = 1
    while user_tries < 4:
        try:
            user_answer = int(input(f"{x} + {y} = "))
            if user_answer == (x + y):
                return True
            else:
                user_tries += 1
                print("EEE")
        except:
            user_tries += 1
            print("EEE")
    print(f"{x} + {y} = {x + y}")
    return False


def start_game(level):
    user_score = 0
    round_count = 1
    while 10 >= round_count:
        x, y = generate_integer(level)
        if create_problem(x, y) == True:
            user_score += 1
        round_count += 1
    return user_score


if __name__ == "__main__":
    main()
