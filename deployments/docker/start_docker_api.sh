
#restart docker containers
pkill screen
docker-compose stop 
docker-compose up -d

#restart api
cd ./../../src/pyrest
screen -dmSL main python api.py -Logfile


