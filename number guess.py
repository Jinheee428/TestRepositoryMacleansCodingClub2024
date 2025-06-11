import random

random_number = random.randint(1, 100)
guess_list = [] 

while True:
    guess_input = input(f"Guess number {len(guess_list) + 1}: ")

    if not guess_input.isdigit():
        print("You must enter a number.")
        continue

    guess = int(guess_input)

    if guess < 1 or guess > 100:
        print("You must enter a number within the range.")
        continue

    guess_list.append(guess)

    if guess == random_number:
        print('Correct!')

    if len(guess_list) == 1:
        print("Wrong! Try again.")
    else:
        prev_diff = abs(random_number - guess_list[-2])
        curr_diff = abs(random_number - guess_list[-1])
        if curr_diff < prev_diff:
            print("Warmer!")
        elif curr_diff > prev_diff:
            print("Colder!")
        else:
            print("Same distance as your last guess!")
