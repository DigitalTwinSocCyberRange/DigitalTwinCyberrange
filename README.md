# DigitalTwinCyberrange

## Installation

1. Install Docker-Compose as described here: https://docs.docker.com/compose/install/
2. Clone the required repositories:
```bash
git clone git@github.com:DigitalTwinSocCyberrange/DigitalTwinCyberrange.git && \
git clone git@github.com:DigitalTwinSocCyberrange/frontendCyberrange.git
 ```

2. Install Python2.7, pip2.7 and required packages by running:
```bash
cd DigitalTwinCyberrange && \
bash setup_python.sh
 ```
3. Setup and start the cyber range
This will start the microservice-infrastructure (Elasticsearch, Filebeat, Logstash, Kibana, Dsiem and Digital Twin), the cyber range frontend (running on port 7080) and the API that connects both

```bash
cd deployments/docker && \
bash init_cyberrange.sh
 ```
4. Enter the ip address or hostname where the cyberrange should be deployed. Usually this is either the default ip address of the maschine or localhost. 192.168.2.54 is used as an example ip address here.
  ```bash
  Enter the Hostname or IP Address where the cyber range will be deployed: 192.168.2.54
   ```

5. To restart the infrastructure you can either run the startup script
 
 ```bash
cd deployments/docker && \
bash start_docker_api.sh
 ```
   or use the API-functionality **http://192.168.2.54:9090/docker_restart**
 
5. To shut down the infrastructure
 
  ```bash
cd deployments/docker && \
bash docker_stop.sh
 ```
  or use the API-functionality **http://192.168.2.54:9090/docker_stop**
 
