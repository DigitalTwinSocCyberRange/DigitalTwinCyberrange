from utils import PLC1_ADDR, PLC2_ADDR, PLC3_ADDR, HMI_ADDR
#from subprocess import Popen, PIPE
from scapy.all import *
import logging
import time

"""
Hereafter a arp scan is performed, it returns all mac addresses that use 10.0.0.3
if more than one different mac addresses are returned a mitm attack is possible 
"""


def arp_scan():
    known_servers=[PLC1_ADDR, PLC2_ADDR, PLC3_ADDR, HMI_ADDR]
    target_ip = "10.0.0.4/24"
    # IP Address for the destination
    # create ARP packet
    arp = ARP(pdst=target_ip)
    # create the Ether broadcast packet
    # ff:ff:ff:ff:ff:ff MAC address indicates broadcasting
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    # stack them
    packet = ether/arp

    result = srp(packet, timeout=3, verbose=0)[0]

    # a list of clients, we will fill this in the upcoming loop
    clients = []

    for sent, received in result:
        clients.append(received.psrc)
        logging.basicConfig(filename='logs/firewall.log',format='%(levelname)s %(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S', level=logging.DEBUG)
    HMI_ADDR+' '+HMI_ADDR+' %(message)s',
    for client in clients:
        if client not in known_servers:
            print("possible attacker: ",client)
            log=HMI_ADDR+" %(ATTACKER_ADDR)s FIREWALL-WARNING: Unkown IP address in network: %(ATTACKER_ADDR)s" %{"ATTACKER_ADDR": client}
            print(log)
            logging.warning(log)
    
	

while True:
    arp_scan()
    time.sleep(30)