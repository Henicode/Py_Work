#generating random number between range game 

import random
x = random.randint(1,20)
guess = int(input("Enter a number between 1 to 20:"))
while x != "guess":
    print
    if guess < x:
        print("guessis LOW")
        guess = int(input("Enter a number between 1 to 20:"))
    elif guess > x:
        print("guess is HIGH")
        guess = int(input("Enter a number between 1 to 20:"))
    else:
        print("CORRECT!")
        break
    print

print("done")
