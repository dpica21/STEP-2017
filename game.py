
guess = int(input("guess a number between 0 and 10:"))


if guess >= 0 and guess <= 3:
    print("wrong")

elif guess > 4 and guess <= 10:
    print("wrong")

elif guess == 4:
    print("correct")

elif guess < 0 or guess > 10:
    print("You can't read")


