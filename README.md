# ON SERVER

Install **python 3.7.9** in your server (+ static valid IP)


Clone repository to your server

go to downloaded folder

create Virtual Environment(Optional - Recommended)

    python -m venv vEnv

active just created Virtual Environment

for windows 

    run vEnv/Script/activate

for linux 

    run source vEnv/bin/activate

import required packages

    pip install -r requirement.txt

edit PortListener.py

    line 7: change TCP_IP to desire IP Address
    line 8: change TCP_PORT to desire Port Number

open Desire Port Number on Firewall

run the program

for windows 

    python main.py
for linux 
    
    python3 main.py

# on Tracker 
###(just Concox GT08 for now)
set server IP to server IP address

set server PORT to server PORT address
