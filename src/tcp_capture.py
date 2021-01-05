import subprocess as sub
import logging
import time
from scapy.all import *

p = sub.Popen(('sudo', 'tcpdump','arp or icmp', '-l'), stdout=sub.PIPE)
logging.basicConfig(filename='tcpdump.log',format='%(asctime)s  %(message)s ', datefmt='%m/%d/%Y %H:%M:%S', level=logging.DEBUG)
#print(p.stdout.read())

for row in iter(p.stdout.readline, b''):
    print(p)
    logging.info(row.rstrip())
    print(row.rstrip())

def check_mitm(pkt):
    logging.info(pkt.summary())
    

#p = sub.Popen(('sudo', 'tcpdump','arp or icmp', '-l'), stdout=sub.PIPE)
#print(type(p))
#pkts = sniff(filter="icmp or arp",prn=lambda x: check_mitm(x))


#pkts = sniff(filter="icmp or arp",prn=lambda x:x.summary())
