chown root $(find conf/filebeat/ conf/filebeat-es/ -name "*.yml")
pkill screen
echo -n "Enter the Hostname or IP Address where the cyber range will be deployed:"
read ip
echo "HOST_IP=$ip" > .env 
bash start_docker_api.sh
