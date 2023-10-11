from art import logo, vs
from game_data import data
import random

def account(person):
    person_name = person['name']
    person_description = person['description']
    person_country = person['country']
    return f"{person_name}, a {person_description}, from {person_country}"

def get_random_account():
    """Get a random account from the data."""
    return random.choice(data)

def control(guess, A, B):
    """The function checks whether your guess true or not."""
    if A > B:
        if guess == "a":
            return True
        else:
            return False
    else:
        if guess == "b":
            return True
        else:
            return False

print(logo)
score = 0
game_end = False
B = get_random_account()

while not game_end:
    A = B
    B = get_random_account()
    while A == B:
        B = get_random_account()
    print(f"Compare A: {account(A)}.")
    print(vs)
    print(f"Against B: {account(B)}.")
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    is_correct = control(guess, A['follower_count'], B['follower_count'])
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        game_end = True
        print(f"Sorry, that's wrong. Final score: {score}")
