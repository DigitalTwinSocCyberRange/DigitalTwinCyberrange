from scapy.all import *
from utils import HMI_ADDR
import logging
import time


#sniff(offline="tcpdump.pcap", prn=check_mitm(), filter='tcp or udp')
#pkts = sniff(offline="tcpdump.pcap",prn = check_mitm())

logging.basicConfig(filename='logs/tcpdump.log',format='%(levelname)s %(asctime)s %(funcName)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S', level=logging.DEBUG)



def tcp_parse(pkt):
    #pkt.show()
    
    protocol_id=pkt.type
    if protocol_id==2054: #protocol is arp
        if (pkt[ARP].op == 1):
            arp_op="ARP-REQUEST"
        elif (pkt[ARP].op == 0):
            arp_op="ARP-REPLY"
        else:
            arp_op="ARP-OTHER"
          
        #log="%(srcip)s %(dstip)s %(arp_op)s: %(summary)s" %{"srcip": pkt[ARP].psrc, "dstip": pkt[ARP].pdst, "arp_op": arp_op, "summary": pkt.summary()}
       
        log="%(srcip)s %(dstip)s %(arp_op)s: %(summary)s" %{"srcip": pkt[ARP].psrc, "dstip": pkt[ARP].pdst, "arp_op": arp_op, "summary": pkt.summary()}
        # this is MAC returned by arp reply, check for mismatch (mitm) print(pkt.hwsrc)
        
     
        if pkt[ARP].psrc != "10.0.0.4": #so that hmi's firewall isn't logged
            logging.info(log)

    elif protocol_id==2048: #protocol is icmp
 
        if (pkt[ICMP].type == 0):
            icmp_type="ICMP-REPLY"
        elif (pkt[ICMP].type == 8):
            icmp_type="ICMP-REQUEST"
        else:
            arp_op="ICMP-OTHER"
        log="%(srcip)s %(dstip)s %(icmp_type)s: %(summary)s" %{"srcip": pkt[IP].src, "dstip": pkt[IP].dst, "icmp_type": icmp_type, "summary": pkt.summary()}
        
        logging.info(log)
       
        #MACs: pkt.src, pkt.dst

    

pkts = sniff(filter="icmp or arp",prn=lambda x: tcp_parse(x))

