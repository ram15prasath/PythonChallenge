secret_num=25
for i in range(0,7):
    user_input=int(input("Enter the Guess"))

    if secret_num == user_input:
        print("Your Guessing is right")
        break
    else:
        print("Your Guessing is wrong")

               