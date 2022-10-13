# Author: Sophia Philips
# GitHub Username: sophiacphilips
# Date: 10/12/2022
# This program asks the user for a number of integers, and then determines the max and min of the group.

#define variables for this test
min=0
max=0
set_nums=0
nums=0

#determine amount of integers user would like to test
print("How many integers would you like to enter?")
amt_ints=int(input())

#ask for amt_ints and input
print("Please enter", amt_ints, "integers.")
nums=int(input())

#max and min are the same if user chooses 1 integer to input
max=nums
min=nums
#create loop for min and max
while set_nums<amt_ints-1:
    nums=int(input())
    if nums>max:
        max=nums
    if nums<min:
        min=nums
    #continue increasing list until amt_ints is reached
    set_nums=set_nums+1

print("min:", min)
print("max:", max)