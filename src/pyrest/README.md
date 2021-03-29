# API

The REST-API is implemented with [Flask](https://flask.palletsprojects.com/en/1.1.x/) and connects the digital twin simulation and the SIEM-system with the LMS of the cyber range. 

## Learning

When a trainee completes a task in which he or she created a correlation rule an API request is triggered which automatically activates the respective rule in Dsiem. 
This is done with the following paths (again 199.999.9.99 is used as a sample ip address for demonstration), called by the frontend, whenever a rule task is marked as completed.

- **199.999.9.99:9090/attacker**
- **199.999.9.99:9090/mitm**
- **199.999.9.99:9090/arp**
- **199.999.9.99:9090/log_manipulation**
- **199.999.9.99:9090/dos**

## Management 

Additionally, the API provides functionalities for the trainer to manage the cyber range training:

- **199.999.9.99:9090/cr_stop** to stop and reset the microservice infrastructure and the frontend of the cyber range 
- **199.999.9.99:9090/cr_start** to restart the microservice infrastructure and the frontend
- **199.999.9.99:9090/restart_dt** to restart the digital twin simulation
