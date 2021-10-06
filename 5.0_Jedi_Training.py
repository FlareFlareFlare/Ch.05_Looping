  #Sign your name:Matthew Flyr

'''
 1. Make the following program work.
   '''  
     print("This program takes three numbers and returns the sum.")
     total = 0

     for i in range(3):
         x = int(input("Enter a number: "))
         total = total + x
     print("The total is:", str(total))
  


'''
  2. Write a Python program that will use a FOR loop to print the even
     numbers from 2 to 100, inclusive.
'''
for i in range(2, 102, 2):
    print(i)




'''
  3. Write a program that will use a WHILE loop to count from
     10 down to, and including, 0. Then print the words Blast off! Remember, use
     a WHILE loop, don't use a FOR loop.
'''
i = 10
while i < 10:
    print(i)
    i = i - 1
    if i == 0:
        print("Blast off!")
        break



'''
  4. Write a program that prints a random integer from 1 to 10 (inclusive).
'''
import random
n = random.randrange(1, 11)
print(n)


'''
  5. Write a Python program that will:
     
     * Ask the user for seven numbers
     * Print the total sum of the numbers
     * Print the count of the positive entries, the count of entries equal to zero,
     and the count of negative entries. Use an if, elif, else chain, not just three
     if statements.
      
'''
pos_total = 0
neg_total = 0
zero_total = 0
total = 0
for i in range(7):
    i = int(input("Number: "))
    total = i + total
    if i > 0:
        pos_total = pos_total + 1
    elif i < 0:
        neg_total = neg_total + 1
    else:
        zero_total = zero_total + 1
print("Total: " + str(total))
print("Total of positive numbers: " + str(pos_total))
print("Total of negative numbers: " + str(neg_total))
print("Total of times entered zero: " + str(zero_total))