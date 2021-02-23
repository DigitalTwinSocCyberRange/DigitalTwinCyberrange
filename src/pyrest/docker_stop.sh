cd ..
whoami
bash deactivate_directives.sh
cd ../deployments/docker
docker-compose stop 
docker container rm elasticsearch 
docker volume rm docker_es-data 


