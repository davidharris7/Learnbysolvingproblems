# CCC06J1 - Canadian Calorie Counting
# https://dmoj.ca/problem/ccc06j1
#


total_calories = 0     
choice = int(input())

if(choice == 1):
    total_calories += 461
if(choice == 2):
    total_calories += 431
if(choice == 3):
    total_calories += 420
if(choice == 4):
    total_calories += 0

choice = int(input())
if(choice == 1):
    total_calories += 100
if(choice == 2):
    total_calories += 57
if(choice == 3):
    total_calories += 70
if(choice == 4):
    total_calories += 0

choice = int(input())
if(choice == 1):
    total_calories += 130
if(choice == 2):
    total_calories += 160
if(choice == 3):
    total_calories += 118
if(choice == 4):
    total_calories += 0

choice = int(input())
if(choice == 1):
    total_calories += 167
if(choice == 2):
    total_calories += 266
if(choice == 3):
    total_calories += 75
if(choice == 4):
    total_calories += 0

print(f"Your total Calorie count is {total_calories}.")