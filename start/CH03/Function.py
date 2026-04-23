#!/usr/bin/env python3
# example workign with Functions
#By 

def check_day(answer):

    #Return response based on user input
    if answer == "y":
        return "Yes it is"
    
    else:
        return "No it is not"
    
    #Get user input and normalize to lowercase
answer = input("Is today a good day? (Y/N): ").lower()

#Repeats result 10 times
for i in range(10):
    result = check_day(answer)
    print(i + 1, result)