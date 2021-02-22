
for var in "$@"
do
    mv ./../../deployments/docker/conf/dsiem/configs/directives_dt_$var.txt ./../../deployments/docker/conf/dsiem/configs/directives_dt_$var.json  
done
docker restart dsiem digital_twin

