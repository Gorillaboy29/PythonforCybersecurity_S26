#!/usr/bin/env python3
# example workign with Loops
#By 

#Ask the user and convert input to lowercase so Y/y both work
answer = input("Is today a good day? (Y/N): ").lower()

#Repeats the answer 10 times
for i in range(10):

#CHeck if user answered yes
    if answer == "y":
        print(i + 1,"Yes it is")

#If anything else (like 'n'), respond no
    else: 
        print("No it is not")


