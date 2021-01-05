from scapy.all import *



#sniff(offline="tcpdump.pcap", prn=check_mitm(), filter='tcp or udp')
#pkts = sniff(offline="tcpdump.pcap",prn = check_mitm())

logging.basicConfig(filename='./logs/tcpdump.log',format='%(asctime)s  %(message)s ', datefmt='%m/%d/%Y %H:%M:%S', level=logging.DEBUG)


def print_and_log(pkt):
    logging.info(pkt.summary())
    print(pkt.summary())

def parse(pkt):
    #pkt.show()
    
    protocol_id=pkt.type
    if protocol_id==2054:
        protocol="arp"
        #print(pkt[ARP].hwsrc)
        srcip=pkt[ARP].psrc
        if srcip != "10.0.0.4": #so that hmi's firewall isn't logged
            print_and_log(pkt)

    elif protocol_id==2048:
        protocol="icmp"
        #print("src ip: ",pkt[IP].src)
        #print("dst ip: ",pkt[IP].dst)
        #print("src mac: ",pkt.src)
        #print("dst mac: ",pkt.dst)
        print_and_log(pkt)
    



pkts = sniff(filter="icmp or arp",prn=lambda x: parse(x))

