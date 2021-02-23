cd /root/DigitalTwinCyberrange/deployments/docker
#restart docker containers
pkill screen
docker-compose stop 
docker-compose up -d

screen -dmSL main /bin/bash kbndashboard-import.sh localhost ../kibana/dashboard-siem.json

#restart api
cd ./../../src
screen -dmSL main bash deactivate_directives.sh -Logfile
cd pyrest
screen -dmSL main python api.py -Logfile

cd ./../../../frontendCyberrange
screen -dmSL main npm run serve -Logfile



