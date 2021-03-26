# DigitalTwinCyberrange

## Installation (for Ubuntu 20.04)

- Install Docker-Compose as described here: https://docs.docker.com/compose/install/
- Clone the required repositories:
```bash
git clone git@github.com:DigitalTwinSocCyberrange/DigitalTwinCyberrange.git && \
git clone git@github.com:DigitalTwinSocCyberrange/frontendCyberrange.git
 ```
 - **Install dependencies for deployment of the frontend:**
```bash
cd frontendCyberrange && \
bash setup_frontend.sh
 ```

- **Install dependencies for deployment of the Flask-Api:**
```bash
cd DigitalTwinCyberrange && \
bash setup_python.sh
 ```
- **Setup and start the cyber range**: This will start the microservice-infrastructure (Elasticsearch, Filebeat, Logstash, Kibana, Dsiem and Digital Twin), the cyber range frontend (running on port 7080) and the API that connects both
```bash
cd deployments/docker && \
bash init_cyberrange.sh
 ```
- Enter the ip address or hostname where the cyberrange should be deployed. Usually this is either the default ip address of the maschine or localhost. 192.168.2.54 is used as an example ip address here.
  ```bash
  Enter the Hostname or IP Address where the cyber range will be deployed: 192.168.2.54
   ```
 - Access the cyber range on **port 7080**: `http://192.168.2.54:7080`
 - to get an idea of the prototype, you can use the demo user (without user data management) **ID=127**
 - Bild von cyber range startseite und 127
 - If you want to conduct a cyber range training with multiple participants and use the scoreboard, please proceed with User Data Manegemnt
## Run and stop the cyber range infrastructure

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
 
