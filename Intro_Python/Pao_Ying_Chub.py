import random
def play_game():
    print("""Let's play Pao Ying Chub with super intellegent AI
        hammer win scissor
        scissor win paper
        paper win hammer
    We will correct the score and conclude when input 'exit'""")
    options = ["hammer", "scissor", "paper"]
    user_score = 0
    bot_score = 0
    print(options)

    while True:
        user_select = input("Choose one! ")
        if user_select == "exit":
            print("-------Summary--------")
            print(f"Your score is : {user_score}")
            print(f"Bot score is : {bot_score}")
            print("----------------------")
            break
        elif user_select not in options:
            print(f"{user_select} not found, please try again!")
            continue

        computer_select = random.choice(options)

        if user_select == computer_select:
            print("Tie!")
        elif user_select == "hammer" and computer_select == "scissor":
            print("You win!")
            user_score += 1
        elif user_select == "scissor" and computer_select == "paper":
            print("You win!")
            user_score += 1
        elif user_select == "paper" and computer_select == "hammer":
            print("You win!")
            user_score += 1
        else:
            print("You lose!")
            bot_score += 1
