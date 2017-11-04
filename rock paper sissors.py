import random 
random_num = random.randint(0,2)
moves = ["rock","paper","sissors"]
computer_move = moves[random_num]

tries = 0

while tries != 3:
    choice = input("Choose rock, paper, or sissors:")
    if choice == computer_move:
        print("tie")
    elif choice =="rock" and computer_move == "sissors":
        print("You win")
    elif choice == "sissors" and computer_move == "paper":
        print("You win")
    elif choice =="paper" and computer_move == "rock":
        print("You win")
    
    else:
        print("you lose")
    tries += 1
print("The move was:", computer_move)






    






        