from scapy.all import *

i = 0
pkt = IP(dst = '10.0.0.2') / TCP(dport=44818)
while i<1000:
   send(pkt)
   #print ("packet sent ", i)
   i = i + 1