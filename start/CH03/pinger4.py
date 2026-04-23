#!/usr/bin/env python3
# Fourth example of pinging from Python
# By 


#import necessary Python modules
import platform
import os

def ping_host(ip):
    #determine the current OS
    current_os = platform.system().lower()
    if current_os == "windows":
        #build our ping command for windows
        ping_cmd = f"ping -n 1 {ip} > nul"
    else: 
        #build pur ping command for other OSs
        ping_cmd = f"ping -c 1 {ip} > /dev/null 2>&1"
    # execute command and capture exit code exit code
    exit_code = os.system(ping_cmd)
    return exit_code

#Define the prefix to begin pinging
ip_prefix = "192.168.0."

#Loop from 0 - 254
for final_octet in range(97, 105):
    #assign IP to ping to a variable
    #adding 1 to final_octet because loop starts at 0
    ip = ip_prefix + str(final_octet + 1)

    #call ping_host function and capture the return value 
    exit_code = ping_host(ip)

    #print results to console only if successful
    if exit_code == 0:
        print("{0} is online".format(ip))