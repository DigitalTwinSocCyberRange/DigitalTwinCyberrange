cd ./../deployments/docker 

chown root $(find conf/filebeat/ conf/filebeat-es/ -name "*.yml")
ip=$(/sbin/ip -o -4 addr list enp1s0 | awk '{print $4}' | cut -d/ -f1)

echo "HOST_IP=$ip" > .env

echo "Please open the following address in your Browser 
${GREEN}http://$ip:7080/${NC}" 

docker-compose up -d > /dev/null 2>&1

#/bin/bash kbndashboard-import.sh localhost ../kibana/dashboard-siem.json > /dev/null 2>&1

cd ./../../src

bash deactivate_directives.sh 

python ./pyrest/api.py 






