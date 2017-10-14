tries = 5
counter = 0

while counter < tries :
 guess = int(input("guess a number between 0 and 10:"))
 counter = counter + 1
 if guess == 4:
  print("right")
 else:
  print("wrong")