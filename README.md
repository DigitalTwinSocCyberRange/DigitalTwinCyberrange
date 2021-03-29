# DigitalTwinSocCyberrange
**DigitalTwinSocCyberrange** is a research project by the University of Regensburg and the Ionian University. This prototype aims to provide training for SOC analysts in a highly realistic scenario making use of the simulation component of the digital twin of an industrial filling plant. In the scenario, an attacker has gained access to the industrial system and performs various attacks (Man-In-The-Middle-Attack, Log-File-Manipulation-Attack and Denial-Of-Service-Attack) to disrupt the filling plant. The components of the industrial system thereby produce log data which are forwarded to a SIEM system. Completing the tasks of the cyber range, a trainee gains knowledge about the selected attacks on the industrial system and how to detect these attacks in a SIEM system by creating correlation rules.
The following video gives an introduction to the project and the learning concept of the cyber range.
<p align="center">
<a href="http://www.youtube.com/watch?feature=player_embedded&v=6czq4r2_kTk
" target="_blank"><img src="https://user-images.githubusercontent.com/56884203/112821430-fd065480-9086-11eb-9498-ed027142e340.png" 
alt="Introduction" width="500" border="2" corder-color="black" /></a> </p> 


**Frontend of the cyber range:**

![Cyberrange_Learning](https://user-images.githubusercontent.com/56884203/112633883-3302c900-8e3a-11eb-9ed7-7d9406a4b715.png)


The concept was evaluated in an extensive **user study**. The results of the user study are presented in the [userStudy repository](https://github.com/DigitalTwinSocCyberrange/userStudy). 


## Architecture of the prototype
- The **Virtual Environment** consists of the simulation component of a Digital Twin which is tailored to the needs of the cyber range scenario. It is implemented with [MiniCPS](https://github.com/scy-phy/minicps), an academic framework for simulating cyber-physical systems which builds upon [Mininet](http://mininet.org). The simulated attacks are performed with [Ettercap](https://www.ettercap-project.org/) and [hping](http://www.hping.org/). The firewall functionalities are implemented with [Scapy](https://scapy.net/).
- The **SIEM** system is realized with [Dsiem](https://www.dsiem.org/), which builds upon [Filebeat, Elasticsearch, Logstash and Kibana](https://www.elastic.co/).
 
The Digital Twin Simulation and the SIEM system of the prototype are based on a microservice architecture realized with **Docker Containers**. 

- The **Learning Management System (LMS)** is implemented with the JavaScript Framework [Vue.js](https://vuejs.org/). The respective source code is stored in the [frontendCyberrange](https://github.com/DigitalTwinSocCyberrange/frontendCyberrange) repository of the project.
- A **[REST-API]((https://github.com/DigitalTwinSocCyberrange/DigitalTwinCyberrange/tree/main/src/pyrest))** implemented with [Flask](https://flask.palletsprojects.com/en/1.1.x/) connects the LMS, the Digital Twin and the SIEM-System
- The user data is stored in a Firestore collection, described in detail [here](#user-data-management)

 <p align="center">
  <img src="https://user-images.githubusercontent.com/56884203/112836327-bb7fa480-909a-11eb-85bc-8307505d52f4.png" />
</p>

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
- Enter the ip address or hostname where the cyber range should be deployed. Usually, th
either the default ip address of the maschine or localhost. 199.999.9.99 is used as an example ip address here.

```bash
Enter the Hostname or IP Address where the cyber range will be deployed: 199.999.9.99
```
 - Access the cyber range on port 7080: **ht<span>tp://</span>199.999.9.99:7080**, to get an idea of the prototype, you can use the demo user (without user data management) **ID=127**
 <p align="center">
  <img src="https://user-images.githubusercontent.com/56884203/112821652-3e96ff80-9087-11eb-805f-aee2533ac3d7.png" width="500" />
</p>

 - If you want to conduct a cyber range training with multiple participants and use the scoreboard, please proceed with [User Data Management](#user-data-management)
## Shutdown
To shut down the infrastructure you can either the use the API-functionality **ht<span>tp://</span>199.999.9.99:9090/stop_cr** or run the shutdown script:
 
 ```bash
cd deployments/docker && \
bash docker_stop.sh
 ```

## Startup
To restart the infrastructure you can either the use the API-functionality **ht<span>tp://</span>199.999.9.99:9090/start_cr** or run the startup script:
 
 ```bash
cd deployments/docker && \
bash start_docker_api.sh
 ```

## User Data Management
User data management enables the gamification aspect of the cyber range with a score board displaying the scores of the other players in order motivate the trainees to engage well in the training. 
 <p align="center">
  <img src="https://user-images.githubusercontent.com/56884203/112821702-4fe00c00-9087-11eb-82bd-ca8c09e51f73.png" width="300" />
</p>

Furthermore, storing the progress of each user in a central database enables the trainer to monitor the conduction of the training and facilitates to evaluate the training after conduction. 
Every trainee initially needs to be assigned the following attributes.

 - **userID**: randomly chosen ID to log into the cyber range, primary key of the Firestore Collection
 - **username**: each userID is assigned a username. This is displayed on the scoreboard
 - **round**: refers to the round of conduction of the cyber range training. The trainee will only see the scores of the players that are playing in the same round as he or she does
 
While taking part in the cyber range training, furthermore, the following data is recorded:

- points: current score of the trainee (out of a maximum score of 101)
- level: number of tasks the trainee has completed
- startTime: timestamp when the trainee first logged in
- taskTimes: time the trainee took to solve a task


### Create Firestore Collection
- Within a Firebase project create **Firestore collection named "cyberrangeDashboard"** as described [here](https://firebase.google.com/docs/firestore/quickstart).
- To link the cyber range to your collection copy the **firebaseConfig** object from the firebase console (Settings -> General) as described [here](https://firebase.google.com/docs/web/setup#config-object) and add it to the configruation file [firebase.js](https://github.com/DigitalTwinSocCyberrange/frontendCyberrange/blob/main/src/firebase.js).
- 
### Create user data
- Create a list containing the user data with a tuple of userID, username and round
 
| userID        | username           | round  |
| ------------- |:-------------:| -----:|
|	7683	|	SudoSven	|	1	|
|	1235	|	SecuritySandra	|	1	|
|	2364	|	RootRuth	|	1	|
|	2346	|	Crewmate	|	2	|
|	5671	|	AnonymousAnna	|	2	|
|	2397	|	MrsRobot	|	2	|


*This example user data set provides user data for two rounds of training with three trainees each.*

- Add all valid userIDs to the [usernames.js](https://github.com/DigitalTwinSocCyberrange/frontendCyberrange/blob/main/src/data/usernames.js) file in the frontend project. *For the previous example this would be adding userIDs 7683, 1235, 2364, 2346, 5671	and 2397.*
- Either add the user data manually to the Firestore collection or use the provided python [scripts](https://github.com/DigitalTwinSocCyberrange/frontendCyberrange/tree/main/FirebaseScripts) as described in the next section to import user data from a csv file to the Firestore collection.

### Import and export of user data with .csv files
- Create a Service Account on Firebase. This can be done on the Firebase Dashboard via Settings -> Service Account -> "Generate Private Key" as described [here]( https://firebase.google.com/docs/admin/setup#python)
- Replace the file [serviceAccount.json](https://github.com/DigitalTwinSocCyberrange/frontendCyberrange/blob/main/FirebaseScripts/serviceAccount.json) with your created key (also naming it serviceAccount.json)
- Replace the sample user data in [userdata.csv](https://github.com/DigitalTwinSocCyberrange/frontendCyberrange/tree/main/userDataScripts/usernames.csv) with your user data sets
- Run import script:
```bash
cd frontendCyberrange/userDataScripts && \
python3 importFromCsv.py
 ```
 - To export user data (points, level, times) after the training, run:
 
 ```bash
cd frontendCyberrange/userDataScripts && \
python3 exportToCsv.py
 ```
