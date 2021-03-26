# DigitalTwinCyberrange
**DigitalTwinSocCyberrange** is a research project by the University of Regensburg and the Ionian University. This prototype aims to provide training for SOC analysts in a highly realisitic environment making use of the simulation component of the digital twin of an industrial filling plant. The concept was evaluated in an extensive user study. The results of the user study are presented in the [userStudy repository](https://github.com/DigitalTwinSocCyberrange/userStudy). 

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
- Enter the ip address or hostname where the cyberrange should be deployed. Usually this is either the default ip address of the maschine or localhost. 199.999.9.99 is used as an example ip address here.

```bash
Enter the Hostname or IP Address where the cyber range will be deployed: 199.999.9.99
```
 - Access the cyber range on port 7080: **ht<span>tp://</span>199.999.9.99:7080**
   
 - to get an idea of the prototype, you can use the demo user (without user data management) **ID=127**
 - Bild von cyber range startseite und 127
 - If you want to conduct a cyber range training with multiple participants and use the scoreboard, please proceed with [User Data Management](#user-data-management)
## Startup/Shutdown

- To restart the infrastructure you can either the use the API-functionality `http://199.999.9.99:9090/restart_cr`or run the startup script:
 
 ```bash
cd deployments/docker && \
bash start_docker_api.sh
 ```
   or 
 
- To shut down the infrastructure you can either the use the API-functionality `http://199.999.9.99:9090/stop_cr`or run the shutdown script:
 
 ```bash
cd deployments/docker && \
bash docker_stop.sh
 ```

## User Data Management
### Create Firestore Collection
- Within a Firebase project create **Firestore collection named "cyberrangeDashboard"** as described [here](https://firebase.google.com/docs/firestore/quickstart)
- To link the cyber range to your collection copy the **firebaseConfig** object from the firebase console (Settings -> General) as described [here](https://firebase.google.com/docs/web/setup#config-object) and add it to the configruation file [firebase.js](https://github.com/DigitalTwinSocCyberrange/frontendCyberrange/blob/main/src/firebase.js)
### Create usernames and IDs
- username/ID combination
- add IDs to the frontend in [usernames.js](https://github.com/DigitalTwinSocCyberrange/frontendCyberrange/blob/main/src/data/usernames.js)
- Now either add the user data manually to the Firestore collection or use the python scripts described in the next section to import user data from a csv file to the Firestore collection

### Import and export of user data with .csv files
- upload csv with ID, username and round to Firestore
- create a Service Account on Firebase. This can be done on the Firebase Dashboard via Settings -> Service Account -> "Generate Private Key" as described [here]( https://firebase.google.com/docs/admin/setup#python)
- Replace the file [serviceAccount.json](https://github.com/DigitalTwinSocCyberrange/frontendCyberrange/blob/main/FirebaseScripts/serviceAccount.json) with your created key (also naming it serviceAccount.json)
- export user data similar to that
