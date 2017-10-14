user_number = int(input("Enter your age:"))

if user_number < 3:
    print("toddler")

elif user_number < 13:
    print("kid")
    
elif user_number < 18:
    print("teenager")
    
elif user_number >= 18 and user_number < 130:
    print("adult") 
    
elif user_number > 129:
    print("ghost")
    