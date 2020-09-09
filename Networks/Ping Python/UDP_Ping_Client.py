## @filename: UDP_Ping_Client.py
## @author: Alex Banning
## @assignment: UDP Ping
## @date: October 9th, 2019
## @description: UDP Client side for ping program.
##               Sends 10 packets to localhost server
##               And records the RTT time for each packet.

#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import random
import time
from socket import *

## Define consts
clientSocket = socket(AF_INET, SOCK_DGRAM)
address = ('localhost', 12000)

## Only send necessary packets
for ProgramCNT in range(10):
    data = "Ping: " + str(ProgramCNT) + " " + time.asctime()
    clientSocket.sendto(data.encode(), address)
    timeCNTStart = time.time()
    clientSocket.settimeout(1)
    
    try:
        returnMessage, returnAddress = clientSocket.recvfrom(1024)
        timeCNTEnd = time.time()
        timeCNT = timeCNTEnd - timeCNTStart
        print ("Packet time: %6.6f\n" % (timeCNT))
        print (returnMessage.decode())
        
    except:
        print ("Message Lost.")
        

clientSocket.close()