# #SWG game: using random,if_elif_else:
# # Snake Water Gun Game in Python
# # The snake drinks the water, the gun shoots the snake, and gun has no effect on water.
#
#
import random
lst=["s","w","g"]
chance=10
no_of_chance=0
human_point=0
computer_point=0

print("You Have 10 Attempts.")
print("Press s:Snake")
print("Press w:Water")
print("Press g:Gun")
while no_of_chance < chance:
    inp=input()
    rand=random.choice(lst)
    if inp==rand:
        print("There's a TIE!!!\n")
    #if user input is s
    elif inp=="s" and rand=="g":
        computer_point = computer_point + 1
        print(f"your guess {inp} and computer guess is {rand} \n")
        print("computer wins 1 point. \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")

    elif inp=="s" and rand=="w":
        human_point = human_point + 1
        print(f"your guess {inp} and computer guess is {rand} \n")
        print("computer wins 1 point. \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")

    # if user enter w
    elif inp == "w" and rand == "s":
        computer_point = computer_point + 1
        print(f"your guess {inp} and computer guess is {rand} \n")
        print("computer wins 1 point. \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")

    elif inp == "w" and rand == "g":
        human_point = human_point + 1
        print(f"your guess {inp} and computer guess is {rand} \n")
        print("computer wins 1 point. \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")

    # if user enter g
    elif inp == "g" and rand == "w":
        computer_point = computer_point + 1
        print(f"your guess {inp} and computer guess is {rand} \n")
        print("computer wins 1 point. \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")


    elif inp == "g" and rand == "s":
        human_point = human_point + 1
        print(f"your guess {inp} and computer guess is {rand} \n")
        print("computer wins 1 point. \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")

    else:
        print("you have input wrong!!! \n")

    no_of_chance = no_of_chance + 1
    print(f"{chance - no_of_chance} is left out of {chance} \n")

print("Game over")

if computer_point == human_point:
    print("Tie")

elif computer_point > human_point:
    print("Computer wins and you loose")

else:
    print("you win and computer loose")

print(f"your point is {human_point} and computer point is {computer_point}")





