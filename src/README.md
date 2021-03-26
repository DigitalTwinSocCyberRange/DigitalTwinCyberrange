# DigitalTwin: Simulation of a filling-plant

The following describes the Digital Twin Simulation of the **DigitalTwinSocCyberrange** prototype. The simulation compoenent represents a filling-plant, consisting of three PLCs (PLC1, PLC2, PLC3), an HMI, an attacker (that has maliciously entered the network) that are connected by a switch.

 <p align="center">
  <img src="https://user-images.githubusercontent.com/56884203/112634397-d48a1a80-8e3a-11eb-890f-e4f5127fcd2b.png" width="500"/>
</p>

*PLC3* reads Sensor3, which measures the liquid level of the bottle to be filled ("*Sensor3-LL-bottle*").
*PLC2* reads Sensor2, which measures flow level of the pipe ("*Sensor2-FL*").
*PLC1* reads Sensor1, which reads the liquid level of the tank ("*Sensor1-LL-tank*") and Actuator1 ("*Actuator1-MV*"). 
*PLC1* decides whether to open or close the motoric valve based on the level of the tank ("*Sensor1-LL-tank*") and the flow level of the pipe ("*Sensor2-FL*") received from PLC2 and the level of the bottle ("*Sensor3-LL-bottle*") received from PLC3. 

An attacker has gained access to the network and performs the following attacks:

- MITM
- DOS




