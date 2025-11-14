secret_num=25
while True:
    user_input=int(input("Enter the Guess"))

    if secret_num == user_input:
        print("Your Guessing is right")
        break
    else:
        print("Your Guessing is wrong")