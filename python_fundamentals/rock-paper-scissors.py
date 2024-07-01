import random as rand

rock = "rock"
paper = "paper"
scissors = "scissors"

rock_lst = [rock, paper, scissors]

computer_choice = rock_lst[rand.randint(0,2)]

user_choice = ""
while (user_choice not in rock_lst):
    user_choice = input("user choice:").lower()

print(computer_choice)
 
if computer_choice == user_choice:
    print ("It's a Tie")
elif computer_choice == "rock" and user_choice == "scissors":
    print ("Computer wins")
elif computer_choice == "rock" and user_choice == "paper":
    print ("You win")