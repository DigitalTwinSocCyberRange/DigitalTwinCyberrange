for var in "$@"
do
    mv ../deployments/docker/conf/dsiem/configs/directives_$var.txt ../deployments/docker/conf/dsiem/configs/directives_$var.json  
done
docker restart dsiem digital_twin

