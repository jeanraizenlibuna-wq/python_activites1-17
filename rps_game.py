import random

choices = ["rock", "paper", "scissor"]

while True:
    print("----HUMAN VS CPU ROCK PAPER SCISSOR-----")
    print("choices:  ", choices)
    user_choice = input("Enter a choice(right quit to exit)").lower()

    if user_choice == "quit":
        print("USAD NA BOI")
        break
if user_choice not in choices:
    print("mali ka boi, pili ka ng iba!")    
computer_choice = random.choice(choices)

if  user_choice == computer_choice:
    print(f"User Choice {user_choice} vs. Computer choice {computer_choice} = DRAW")
elif(
    user_choice == "rock" and computer_choice == "scissor"
or user_chocie == "scissor" and computer_choice == "paper"
or user_choice == "paper" and computer_choice
== "rock")
print(f"User Choice {user_choice} vs. Computer choice {computer choice} = USER WINS")  