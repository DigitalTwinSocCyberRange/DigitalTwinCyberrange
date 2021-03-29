# Digital Twin Simulation: the filling-plant scenario

The following describes the Digital Twin Simulation of the **DigitalTwinSocCyberrange** prototype. The simulation component represents a filling-plant, consisting of three PLCs (PLC1, PLC2, PLC3), an HMI, an attacker (that has maliciously entered the network) that are connected by a switch.

 <p align="center">
  <img src="https://user-images.githubusercontent.com/56884203/112801494-40ee5f00-9071-11eb-9e71-d55030ddfa73.png" width="500"/>
</p>

*PLC3* reads Sensor3, which measures the liquid level of the bottle to be filled ("*Sensor3-LL-bottle*").
*PLC2* reads Sensor2, which measures the flow level of the pipe ("*Sensor2-FL*").
*PLC1* reads Sensor1, which reads the liquid level of the tank ("*Sensor1-LL-tank*") and Actuator1 ("*Actuator1-MV*"). 
*PLC1* decides whether to open or close the motoric valve based on the level of the tank ("*Sensor1-LL-tank*") and the flow level of the pipe ("*Sensor2-FL*") received from PLC2 and the level of the bottle ("*Sensor3-LL-bottle*") received from PLC3. 

An attacker has gained access to the network and performs the following attacks:

- **[Man-In-The-Middle-Attack](./mitm_attack.sh)**: the attacker sniffs the network traffic between PLC1 and PLC3 and interrupts it with arp-spoofing. The attack is implemented with [ettercap](https://www.ettercap-project.org/).
- **[Log-Manipulation-Attack](./rm_attack.sh)**: the attacker aims to disrupt the log correlation of the SIEM-system by manipulating the log file in which PLC1 stores its log data. The attack is implemented with a bash script, that removes logs/plc1.log.
- **[Denial-of-Service-Attack](./dos_attack.sh)**: the attacker aims to stop PLC1 from working by flooding it with ICMP packages. The attack is implemented with [hping3](http://www.hping.org/).

To have the industrial system producing consistent log data over the lifetime of the cyber range all attacks are performed periodically.

A **firewall** is running on the HMI capturing selected TCP traffic and detecting certain abnormalities. Thereby it logs every captured ICMP and ARP package and produces a warning log

- if an unknown ip address is detected in the network 
- if the response to an ARP-request is ambiguous (duplicate ip address configured)

The functionalities of the firewall are implemented with [Scapy](https://scapy.net/) in [tcp_capture.py](./tcp_capture.py) and [firewall.py](./firewall.py)

Additionally, each PLC produces a warning log, when its log file was removed and therefore needs to be newly created.

