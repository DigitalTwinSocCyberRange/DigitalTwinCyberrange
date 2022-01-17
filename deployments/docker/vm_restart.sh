docker-compose stop
sudo docker container rm elasticsearch
sudo docker volume rm docker_es-data
docker-compose up -d
cd ./../../src
cd pyrest
screen -dmSL main bash deactivate_directives.sh -Logfile


