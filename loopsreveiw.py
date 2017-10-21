import random
number = random.randint(0,10)
num_guesses = 3

for i in range(num_guesses):
    guess = int(input("What is your guess:"))
    if(number == guess):
        print ("you win")
    else:
        print("you lose")
        
print("\nMagic number: ", number)