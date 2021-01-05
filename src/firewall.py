from utils import PLC1_ADDR, PLC2_ADDR, PLC3_ADDR, HMI_ADDR
from subprocess import Popen, PIPE
from scapy.all import *
import logging
import time

"""
Hereafter a arp scan is performed, it returns all mac addresses that use 10.0.0.3
if more than one different mac addresses are returned a mitm attack is possible 
os.system("arping -C 3 10.0.0.3 > arp_res.txt")

with open("arp_res.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 
ans=[[],[],[]]
mac=[]
for i in range (1,4):
        for word in content[i].split():
            ans[i-1].append(word)
for j in ans:
    mac.append(j[3])
    
if not (all(element==mac[0] for element in mac)):
    print("MITM detected")
else:
    print("everything ok")
"""




def arp_scan(ip):

    request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip)

    ans, unans = srp(request, timeout=2, retry=1)
    result = []

    for sent, received in ans:
        result.append({'IP': received.psrc, 'MAC': received.hwsrc})
    return result

def arp_scan_2():
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
    #print(result)
    # a list of clients, we will fill this in the upcoming loop
    clients = []
    #print(known_servers)
    for sent, received in result:
        #print(sent, received)
        # for each response, append ip and mac address to `clients` list
        #clients.append({'ip': received.psrc, 'mac': received.hwsrc})
        clients.append(received.psrc)
    # print clients
    #print("Available devices in the network:")
    #print("IP" + " "*18+"MAC")
    #print(clients)
    logging.basicConfig(filename='./logs/firewall.log', format='%(levelname)s %(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S', level=logging.DEBUG)
    for client in clients:
        if client not in known_servers:

            print("possible attacker: ",client)
            logging.warning("Unkown IP address in network: "+ client)
	

arp_scan_2()