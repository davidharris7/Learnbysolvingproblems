# ccc15j1 - Special Day
# https://dmoj.ca/problem/ccc15j1

print("enter month")
month = int(input())

print("enter day")
day = int(input())

if month < 2 or (month == 2 and day <18):
    print("Before")
elif month > 2 or (month == 2 and day > 18):
    print("After")
else:
    print("Special")




# # My Fist attempt
# if month < 2:
#     print("Before ")
# elif month > 2:
#     print("After")
# elif day < 18:
#      print("Before")
# elif day > 18:
#     print("After")
# else:
#     print("Special")
#