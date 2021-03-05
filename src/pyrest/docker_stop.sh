cd ..
bash deactivate_directives.sh
screen -X -S frontend quit
cd ../deployments/docker
sudo docker-compose stop 
sudo docker container rm elasticsearch 
sudo docker volume rm docker_es-data 


