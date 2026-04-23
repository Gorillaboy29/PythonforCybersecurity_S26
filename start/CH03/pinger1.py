#!/usr/bin/env python3
# First example of pinging from Python
# By 

#import necessary Python modules
import platform
import os

#assign IP to ping to a variable
ip = "127.0.0.1"
#Build our ping command
ping_omd = f"ping -o 1 -w 2 {ip} > /dev/null 2 >&1"
# Execute command and capture exit code
exit_code = os.system(ping_omd)
#Print results to console
print(exit_code)