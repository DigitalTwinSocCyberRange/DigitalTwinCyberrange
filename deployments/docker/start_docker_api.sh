ip=$(ip addr show enp1s0 | grep "inet\b" | awk '{print $2}' | cut -d/ -f1)
echo "HOST_IP=$ip" > .env
#uncomment if interface for cyber range is known to retrieve ip address automatically

#restart docker containers
pkill screen
docker-compose stop
sudo docker container rm elasticsearch
sudo docker volume rm docker_es-data
docker-compose up -d

screen -dmSL main /bin/bash kbndashboard-import.sh localhost ../kibana/dashboard-siem.json

#restart api
cd ./../../src
cd pyrest
screen -dmSL main bash deactivate_directives.sh -Logfile
screen -dmSL main python api.py -Logfile
touch a.txt
cd ./../../../frontendCyberrange
touch b.txt
screen -dmSL main npm run serve -Logfile



