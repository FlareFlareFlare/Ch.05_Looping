'''
COIN TOSS PROGRAM
-----------------
1.) Create a program that will print a random 0 or 1.
2.) Instead of 0 or 1, print heads or tails. Do this using if statements. Don't select from a list.
3.) Add a loop so that the program does this 50 times.
4.) Create a running total for the number of heads and the number of tails and print the total at the end.
'''

import random
heads_total = 0
tails_total = 0
for i in range(50):
    x = random.randint(0,1)
    if x == 0:
        print("Heads!")
        heads_total += 1
    else:
        print("Tails")
        tails_total += 1
print("Amount of times heads: " + str(heads_total))
print("Amount of times tails: " + str(tails_total))









