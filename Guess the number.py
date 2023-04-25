import random

# User will guess the random number from computer

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print("Too low")
        elif guess>random_number:
            print("Too high")
    print(f"Congrats, Correct number is {random_number}")
#guess(10)

# Computer will guess the random number from user.

def computer_guess(x):
    low =1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low
        feedback = input(f'Is {guess} too high(H), too low (L),or correct(C) ').lower()
        if feedback =='h':
            high = guess-1
        elif feedback == 'l':
            low = guess+1
    print(f"Congrats, You guessed it right. !! Correct number is {guess}")

computer_guess(100)