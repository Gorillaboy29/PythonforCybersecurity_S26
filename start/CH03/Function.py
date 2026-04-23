#!/usr/bin/env python3
# example workign with Functions
#By 

def check_day(answer):
    if answer == "y":
        return "Yes it is"
    else:
        return "No it is not"
answer = input("Is today a good day? (Y/N): ").lower()

for i in range(10):
    result = check_day(answer)
    print(i + 1, result)