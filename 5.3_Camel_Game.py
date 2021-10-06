'''
This is a two stage star wars game. It has an Oregon Trail type first stage, with seemingly meaningless choices sprinkled in.
There is also a second stage that in which based on your moral choices you might be forced to fight darth maul.
Otherwise you will be put into some dialouge options.
SPOILERS!!!!!
First ending: Choosing to quit at the very beginning. This ending can happen by pressing q in the actions.
Second ending: Making it through Dathomir then giving up. This can happen by pressing Y when asked to give up.
Third ending: Beating Darth Maul when forced to fight him. This can happen by raising your political action and then beating Darth Maul when forced to fight him.
Fourth ending: Rebelling aganist the council. This can happen by answering A for all of the Darth Maul dialouges.
Fifth ending: Being accepted amongst the council. This can happen by answering B for all of the Darth Maul dialouges.
Sixth ending: Getting killed by Darth Maul instantly. This can happen by answering C for all of the Darth Maul dialouges.
Seventh ending: Killing Darth Maul in the dialouge section. This can happen by answering with different options in the Darth Maul dialouge and then beating him when you fight him.
'''
#imports the needed commands
import random
import time
print("You are in training to become a Jedi. In order for the council to accept you, you must complete the impossible task.")
print()
print("After you have failed in pretty much every combat category, they have considered throwing you out.")
print("But your strategic mind is just so extraoridnary that they disigned the perfect challenge for you.")
print()
goal = print("YOUR GOAL: You are stuck in Dathomir. Home of the zabraks and the night sisters. We are currently in very shakey relations with them. You must find your way off Dathomir without causing a war.")
print()
print("Time to begin. You will be given a Taun-taun for transportation and a little bit of water.")
print("Also, some zabraks heard of your situation and are trying to kill you.")
print("Make sure to check your status constantly incase the zabraks sneak up on you.")
print("Prove the council wrong. But don't send us into another war.")
#these are the instructions and story to the game
determination = False
miles_traveled = 0
thirst = 0
transportation_tired = 0
zabraks_chasing = -20
drinks_of_water = 5
politic_action = 0
darth_maul = False
#these are all of my variables
while not determination:
    if miles_traveled >= 200:
        determination = True
        time.sleep(.25)
        print("You made it out of Dathomir's landscape.")
        time.sleep(.25)
        print("There is a spaceship ahead, but you have an uneasy feeling.")
        time.sleep(.25)
        print("This is your final chance to give up.")
        time.sleep(.25)
        give_up = input("Do you want to give up? (Y/N): ")
        time.sleep(.25)
        if give_up.upper() == "Y":
            print("The order still didn't accept you, you become a street sweeper.")
            break
        elif give_up.upper() == "N":
            print("On to the next challenge, then.")
            darth_maul = True
            break
#this checks if you have gotten through the first stage of the game.
    if transportation_tired > 8:
        print("Your transportation is dead.")
        determination = True
        break
    elif transportation_tired >= 6:
        print("Your Taun-taun isn't looking so good.")
    if thirst > 6:
        print("You died of thirst!")
        determination = True
        break
    elif thirst >= 4:
        print("You are getting very thirsty!")
    if zabraks_chasing >= 0:
        print("The zabraks caught up to you and killed you.")
        determination = True
        break
    elif zabraks_chasing > -10:
        print("You start to hear screams in the distance.")
#these check to see if you are dead or if you need a warning.
    print("A. Drink from your deteriorating water supply.")
    time.sleep(.25)
    print("B. Ahead moderate speed.")
    time.sleep(.25)
    print("C. Ahead full speed.")
    time.sleep(.25)
    print("D. Stop for the night. Dathomir comes alive at night.")
    time.sleep(.25)
    print("E. Status check.")
    time.sleep(.25)
    print("Q. Quit")
    time.sleep(.25)
#this prints all the available actions
    user_choice = input("Choose your action: ")
    if user_choice == "CHEAT":
        miles_traveled += 200
#this takes you straight to the second stage of the game. Made for testing and showing people the end.
    elif user_choice.upper() == "Q":
        print("So you have given up. You are cast out of the order and forgotten about. You now barely get by as a bounty hunter.")
        determination = True
#checks if the user ever wants to quit
    elif user_choice.upper() == "E":
        print("Miles travled: " + str(miles_traveled))
        print("Drinks of water left: " + str(drinks_of_water))
        print("Miles the zabraks are behind: " + str(zabraks_chasing))
        print("Thirst: " + str(thirst))
        print("Taun-tuan condition: " + str(transportation_tired))
#prints out all the stats that have some relevance.
    elif user_choice.upper() == "D":
        transportation_tired = 0
        zabraks_chasing += 3
        print("Your Taun-taun is very happy, however you can start to see a campfire behind you in the distance.")
        dathomir_death = random.randrange(1,10)
        if dathomir_death == 3:
            print("A night sister sees you and kills you in your sleep.")
            determination = True
#lets the user rest, and giving them a ten percent chance of getting killed.
    elif user_choice.upper() == "C":
        miles_traveled += random.randrange(10,20)
        print("Miles travled: " + str(miles_traveled))
        thirst += 1
        transportation_tired += random.randrange(1,3)
        zabraks_chasing -= 2
        dathomir_death = random.randrange(1, 20)
        if dathomir_death == 7:
            print("You end up going so fast that you don't stop to see a cliff. You and your Taun-taun fall and die.")
            determination = True
#lets the user go fast, but also comes at a risk.
    elif user_choice.upper() == "B":
        miles_traveled += random.randrange(5,12)
        print("Miles travled: " + str(miles_traveled))
        thirst += 1
        transportation_tired += 1
        zabraks_chasing += 2
        dathomir_death = random.randrange(1, 5)
        if dathomir_death == 3:
            print("You find a dying zabrak with lots of water on him.")
            moral_choice1 = input("Do you want to kill him and take his water? (Y for yes, N for no.): ")
            if moral_choice1.upper() == "Y":
                politic_action += 5
                drinks_of_water += 5
            elif moral_choice1.upper() == "N":
                print("You did the right thing.")
            else:
                print("You can't escape the choice.")
                politic_action += 2
#the safe option to move forward. Also gives the user their first moral choice.
    elif user_choice.upper() == "A":
        if drinks_of_water > 0:
            drinks_of_water -= 1
            thirst = 0
            print("You are no longer thirsty!")
            moral_choice2 = random.randrange(1,5)
            if moral_choice2 == 2:
                print("You see a stranger's house. They might have water and shelter.")
                moral_choice2_2 = input("Do you break in? (Y/N): ")
                if moral_choice2_2.upper() == "Y":
                    print("You get more water and are better rested.")
                    drinks_of_water += 5
                    transportation_tired = 0
                    politic_action += 5
                elif moral_choice2_2.upper() == "N":
                    print("You walk past.")
                else:
                    politic_action += 2
#this gives you the second moral choice as well as lets you drink water.
#main while loop for getting through dathomir
#this ending if/else statment takes you to a second while loop
player_health = 100
darth_maul_health = 1000
darth_maul_rage = 5
council_action = 0
#This leads to a dialouge section as well as a boss fight with five seperate endings.
if darth_maul == True:
    print("You move toward your only way off the planet. You are very uneasy about the situation.")
    print("You would love to just go back home, but that is not an option right now.")
    print("You feel so close to finally being accepted by the council")
    print("You put your hand on the handle of your light saber.")
    print()
    print("Standing inside the ship, between your only way out is Darth Maul.")
    print("He was presumed to be dead for years now, but there he is, half robotic and filled with hate.")
    if politic_action <= 10:
        print("Darth Maul stares into with rage.")
        print("You try and reason with him.")
        print("A. We both want the same thing. To see the order fall.")
        print("B. You and I have no business with each other.")
        print("C. Just let me pass, I need to become a Jedi.")
        user_choice3 = input("What do you say?: ")
        if user_choice3.upper() == "A":
            print("You: 'We both want the same thing. To see the order fall.'")
            print("Darth Maul lessens his hold on his lightsaber, but his eyes look only angrier.")
            council_action += 1
        elif user_choice3.upper() == "B":
            print("You: 'You and I have no business with each other.'")
            print("Darth Maul says nothing, but he might see your point.")
            darth_maul_rage = darth_maul_rage - 1
        elif user_choice3.upper() == "C":
            print("You: 'Just let me pass, I need to become a Jedi.'")
            print("Darth Maul: 'I remember the one I met who was training to be a Jedi.'")
            print("He grows angrier.")
            darth_maul_rage += 3
        print("You two still face each other, neither showing any signs of backing off.")
        print("A. You and I could team up, storm Coruscant, and bring down the order.")
        print("B. We can drop the light sabers and walk the other way.")
        print("C. I NEED to complete this mission, it is my last chance!")
        user_choice3 = input("What do you say?: ")
        if user_choice3.upper() == "A":
            print("You: 'You and I could team up, storm Coruscant, and bring down the order.'")
            print("Darth Maul's expression starts to turn from rage to understanding.")
            council_action += 1
        elif user_choice3.upper() == "B":
            print("You: 'We can drop the light sabers and walk the other way.'")
            print("Darth Maul: 'If only if were that easy.' His expression lightens.")
            darth_maul_rage -= 1
        elif user_choice3.upper() == "C":
            print("You: 'I NEED to complete this mission, it is my last chance!'")
            print("Darth Maul: 'You always can have another chance.'")
            darth_maul_rage += 2
        print("The tension is the room is increasing.")
        print("A. With your combat skills, and my mind, we couldn't be stopped!!!")
        print("B. I refuse to fight you, it is unreasonable.")
        print("C. You could never understand!")
        user_choice3 = input("What do you say?: ")
        if user_choice3.upper() == "A":
            print("You: 'With your combat skills, and my mind, we couldn't be stopped!!!'")
            print("Darth Maul says nothing, but the rage in his eyes is redirected.")
            council_action += 1
        elif user_choice3.upper() == "B":
            print("You: 'I refuse to fight you, it is unreasonable.'")
            print("Darth Maul stays silent, but seems to agree.")
            darth_maul_rage -= 1
        elif user_choice3.upper() == "C":
            print("You: 'You could never understand!'")
            print("Darth Maul is very angry, you can feel the force in the air manipulate.")
            darth_maul_rage += 2
        if darth_maul_rage >= 9:
            print("You got the bad ending.")
            print()
            print("Darth Maul was driven into so much rage that he moved faster than your eye could see and cut you in half. You are quickly forgotten about.")
        elif council_action >= 2:
            print("You got the intermediate ending.")
            print()
            print("You and Darth Maul team up. You guys go to Coruscant. Unfortunatly, you aren't very combaitly talented. You are killed almost immeadiatly.")
            print("However, Darth Maul takes the council and sends the galaxy into another empire ruled by himself and only himself.")
        elif darth_maul_rage <= 2:
            print("You got the good ending.")
            print()
            print("You talk Darth Maul down, and you take the ship back to the council. They accept you and you become a Jedi.")
        else:
            print("Darth Maul is still mad and not backing off. You have no choice but to fight him.")
            while darth_maul:
                screwed = random.randrange(1, 10)
                if screwed == 5:
                    print("Darth Maul attacks before you have time to think.")
                    player_health -= 10
                time.sleep(.25)
                print("A. Attack")
                time.sleep(.25)
                print("B. Defend")
                time.sleep(.25)
                print("C. Reason")
                time.sleep(.25)
                print("Health: " + str(player_health))
                time.sleep(.25)
                print("Darth Maul :" + str(darth_maul_health))
                time.sleep(.25)
                user_choice2 = input("What is your action?: ")
                if user_choice2.upper() == "C":
                    print("You: 'We don't need to fight.' Darth Maul: '...'")
                    print()
                    print("That didn't seem effective")
                    print("Darth Maul attacks!")
                    player_health = player_health - 50
                    if player_health <= 0:
                        print("You have died.")
                        darth_maul = False
                        break
                    elif darth_maul_health <= 0:
                        print("You have defeated Darth Maul.")
                        print()
                        print("You kill Darth Maul. The order finally accepts you, however Darth Maul's death sends the galaxy into a war.")
                        print("Blamed for the war, you do not last long.")
                        darth_maul = False
                        break
                elif user_choice2.upper() == "B":
                    print("You block with your light saber.")
                    print("Darth Maul sees this and counters, but most of the damage is blocked.")
                    player_health = player_health - 2
                    if player_health <= 0:
                        print("You have died.")
                        darth_maul = False
                        break
                    elif darth_maul_health <= 0:
                        print("You have defeated Darth Maul.")
                        print()
                        print("You kill Darth Maul. The order finally accepts you, however Darth Maul's death sends the galaxy into a war.")
                        print("Blamed for the war, you do not last long.")
                        darth_maul = False
                        break
                elif user_choice2.upper() == "A":
                    print("You attack Darth Maul")
                    attack_damage = random.randrange(1, 50)
                    counter_attack = random.randrange(1, 5)
                    if counter_attack == 3:
                        print("Darth Maul launches an attack before you can even think.")
                        player_health -= 5
                    darth_maul_health = darth_maul_health - attack_damage
                    if attack_damage > 40:
                        print("You strike so hard, he is stunned and you attack again")
                        attack_damage = random.randrange(1, 75)
                        darth_maul_health = darth_maul_health - attack_damage
                        if attack_damage > 30:
                            attack_again = input("Do you want to attack again? (Y/N): ")
                            if attack_again.upper() == "Y":
                                print("Darth Maul counters and strikes you.")
                                player_health = player_health - 20
                            elif attack_again.upper() == "N":
                                print("Darth Maul expects you to attack again, but you don't.")
                    if player_health <= 0:
                        print("You have died.")
                        darth_maul = False
                        break
                    elif darth_maul_health <= 0:
                        print("You have defeated Darth Maul.")
                        print()
                        print("You kill Darth Maul. The order finally accepts you, however Darth Maul's death sends the galaxy into a war.")
                        print("Blamed for the war, you do not last long.")
                        darth_maul = False
                        break
#the easier of the two boss fights is below this
    else:
        while darth_maul:
            screwed = random.randrange(1,10)
            if screwed == 5:
                print("Darth Maul attacks before you have time to think.")
                player_health -= 10
            time.sleep(.25)
            print("A. Attack")
            time.sleep(.25)
            print("B. Defend")
            time.sleep(.25)
            print("C. Reason")
            time.sleep(.25)
            print("Health: " + str(player_health))
            time.sleep(.25)
            print("Darth Maul :" + str(darth_maul_health))
            time.sleep(.25)
            user_choice2 = input("What is your action?")
            time.sleep(.25)
            if user_choice2.upper() == "C":
                print("You: 'We don't need to fight.' Darth Maul: '...'")
                print()
                print("That didn't seem effective")
                print("Darth Maul attacks!")
                player_health = player_health - 50
                if player_health <= 0:
                    print("You have died.")
                    darth_maul = False
                    break
                elif darth_maul_health <= 0:
                    print("You have defeated Darth Maul.")
                    print()
                    print("Unfortunately, the order does not accept what you have done and casts you out.")
                    darth_maul = False
                    break
            elif user_choice2.upper() == "B":
                print("You block with your light saber.")
                print("Darth Maul sees this and counters, but most of the damage is blocked.")
                player_health = player_health - 2
                if player_health <= 0:
                    print("You have died.")
                    darth_maul = False
                    break
                elif darth_maul_health <= 0:
                    print("You have defeated Darth Maul.")
                    print()
                    print("Unfortunately, the order does not accept what you have done and casts you out.")
                    darth_maul = False
                    break
            elif user_choice2.upper() == "A":
                print("You attack Darth Maul")
                attack_damage = random.randrange(1,100)
                counter_attack = random.randrange(1,10)
                if counter_attack == 7:
                    print("Darth Maul launches an attack before you can even think.")
                    player_health -= 5
                    continue
                darth_maul_health = darth_maul_health - attack_damage
                if attack_damage > 70:
                    print("You strike so hard, he is stunned and you attack again")
                    attack_damage = random.randrange(1, 100)
                    darth_maul_health = darth_maul_health - attack_damage
                    if attack_damage > 30:
                        attack_again = input("Do you want to attack again? (Y/N): ")
                        if attack_again.upper() == "Y":
                            print("Darth Maul counters and strikes you.")
                            player_health = player_health - 20
                        elif attack_again.upper() == "N":
                            print("Darth Maul expects you to attack again, but you don't.")
                if player_health <= 0:
                    print("You have died.")
                    darth_maul = False
                    break
                elif darth_maul_health <= 0:
                    print("You have defeated Darth Maul.")
                    print()
                    print("Unfortunately, the order does not accept what you have done and casts you out.")
                    darth_maul = False
                    break