#!/usr/bin/env python3
# Third example of pinging from Python
# By 


# import necessary Python Modules
import platform
import os

#Define the prefix to begin pinging
ip_prefix = "192.168.0."
#Determine the current OS
current_os = platform.system().lower()
# Loop from 0-254
for final_octet in range(95, 105):
    #Assign IP to ping to a variable
    # Adding 1 to final_octet because loop start at 0
    ip = ip_prefix + str(final_octet + 1)
    if current_os == "windows":
        #Build our ping command for windows
        ping_cmd = f"ping -n 1 {ip} > nul" 
    else: 
        #Build our ping command for other OSs
        ping_cmd = f"ping -c 1 {ip} > /dev/null 2>&1"

    #Execute command  and capture exit node
    exit_code = os.system(ping_cmd)
    #Print results to console only if succesful
    if exit_code == 0:
        print("{0} is online".format(ip))
    
