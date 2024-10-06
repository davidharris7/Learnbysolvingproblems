# CCC18J1 - Telemarketer or not?
# https://dmoj.ca/problem/ccc18j1

# ASSUMPTIONS
# Four digit phone numbers
# Telemarketer
#   first digit is 8 or 9
#   fourth digit is 8 or 9
#   second and third digits are the same
#
# INPUT Four lines
# 
# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
# num4 = int(input())

num1 = 5
num2 = 6
num3 = 6
num4 = 8

if num1 == 8 or num1 == 9:
    print("ignore")
elif num2 == num3:
    print('ignore')
elif num4 == 8 or num4 ==9:
    print('ignore')
else:
    print('answer')
    