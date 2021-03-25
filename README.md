# DigitalTwinCyberrange

## Installation (for Ubuntu 20.04)

- Install Docker-Compose as described here: https://docs.docker.com/compose/install/
- Clone the required repositories:
```bash
git clone git@github.com:DigitalTwinSocCyberrange/DigitalTwinCyberrange.git && \
git clone git@github.com:DigitalTwinSocCyberrange/frontendCyberrange.git
 ```
 - Install latest version of npm and packages required for deployment of the frontend:
```bash
cd frontendCyberrange && \
sudo apt install nodejs && \
npm install -g npm@latest && \
npm install && \
cd ..
 ```

- Install Python2.7, pip and packages required for the api:
```bash
cd DigitalTwinCyberrange && \
bash setup_python.sh
 ```
- Setup and start the cyber range
```bash
cd deployments/docker && \
bash init_cyberrange.sh
 ```
> This will start the microservice-infrastructure (Elasticsearch, Filebeat, Logstash, Kibana, Dsiem and Digital Twin), the cyber range frontend (running on port 7080) and the API that connects both

- Enter the ip address or hostname where the cyberrange should be deployed. Usually this is either the default ip address of the maschine or localhost. 192.168.2.54 is used as an example ip address here.
  ```bash
  Enter the Hostname or IP Address where the cyber range will be deployed: 192.168.2.54
   ```

- To restart the infrastructure you can either run the startup script
 
 ```bash
cd deployments/docker && \
bash start_docker_api.sh
 ```
   or use the API-functionality `http://192.168.2.54:9090/restart_cr`
 
- To shut down the infrastructure
 
  ```bash
cd deployments/docker && \
bash docker_stop.sh
 ```
  or use the API-functionality `http://192.168.2.54:9090/stop_cr`
 
