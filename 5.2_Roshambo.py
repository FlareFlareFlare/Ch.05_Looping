'''
ROSHAMBO PROGRAM
----------------

Create a program that randomly prints 1, 2, or 3.
Expand the program so it randomly prints rock, paper, or scissors using if statements. Don't select from a list.
Add to the program so it first asks the user their choice as well as if they want to quit.
(It will be easier if you have them enter 1 for rock, 2 for paper, and 3 for scissors.)
Add conditional statements to figure out who wins and keep the records
When the user quits print a win/loss record

'''
import random
done=False
count=0
bot_score=0
user_score=0
print("Enter 1 for rock, 2 for paper, 3 for scissors, and 4 to quit")
while not done:
    answer = random.randrange(1,4)
    user_answer = int(input("Choose Rock, paper, or scissors. (Rock = 1, paper = 2, scissors = 3: "))
    if user_answer == 4:
        print("Done")
        done=False
        break
    elif user_answer != 4:
       count+=1
    if user_answer == 1 and answer == 1:
        print("You tied!")
        bot_score+=1
        user_score+=1
    elif user_answer == 2 and answer == 2:
        print("You tied!")
        bot_score+=1
        user_score+=1
    elif user_answer == 3 and answer == 3:
        print("You tied!")
        bot_score+=1
        user_score+=1
    elif user_answer == 1 and answer == 2:
        print("You lost!")
        bot_score+=1
    elif user_answer == 3 and answer == 1:
        print("You lost!")
        bot_score+=1
    elif user_answer == 2 and answer == 3:
        print("You lost!")
        bot_score+=1
    elif user_answer == 1 and answer == 3:
        print("You won!")
        user_score+=1
    elif user_answer == 2 and answer == 1:
        print("You won!")
        user_score+=1
    elif user_answer == 3 and answer == 2:
        print("You won!")
        user_score+=1
    elif user_answer != 1 or user_answer != 2 or user_answer != 3 or user_answer != 4:
        print("Enter a number 1, 2, 3, or 4")
print("The bot had " + str(bot_score) + " wins, and you had " + str(user_score) + " wins.")
if bot_score > user_score:
    print("You ended up losing the war")
elif bot_score < user_score:
    print("You won the war")
else:
    print("You guys tied")
print("You played " + str(count) + " times")








