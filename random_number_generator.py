import sys
from random import randrange

def operation():
    i = 0
    random_number = randrange(101)
    while i<5:
        i = i + 1
        guess = int(input("Enter your Guess: \t"))
        try:
            if not(guess>=1 & guess<=100):
                print("Try again with a valid input between 1-100.")
                i = 0     
                operation()
        except:
            pass
        else:
            if guess < random_number:
                print("your guess is less than the actual number.")
            elif guess > random_number:
                print("your guess is more than the actual number.")
            else:
                print(f"You guessed the number, it is {random_number}.")
                print("Game Over!")
            if i == 5 or guess== random_number:
                feedback = int(input("Press 0 if you want to exit and 1 if you want to play a new game \t"))
                if feedback==0:
                    break
                elif feedback==1:
                    i = 0
                    random_number = randrange(101)
                else:
                    print("Give a proper feedback, 1 or 0.")


print("\n")
print("Guess the random number from 1-100 within 5 tries.")
operation()







        



