import random
print("Welcome to the number Guessing Game")
secret_number=random.randint(1,100)
user_input=int(input("Enter your Guess:"))
attempt=0
while True:
    if(user_input < 1 or user_input > 100):
        print("Valid Input")
        attempt+=1
        continue


    if (user_input < secret_number):
        print(f"The number is greater than {user_input}")
        
    elif (user_input > secret_number):
        print(f"The number is Lesser than {user_input}")
        
    else:
        print(f"congrats You guessed correctly{user_input}") 
        print(f"You guessed {secret_number} in {attempt} attempts.")   