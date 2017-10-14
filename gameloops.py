 #for i in range(100):
   # print(i)
guess = int(input("guess a number between 0 and 10:"))
while guess > 4 or guess < 4:
 if guess == 4:
  print("right")
 else:
  print("wrong")