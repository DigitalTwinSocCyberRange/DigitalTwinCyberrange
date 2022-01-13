find ../../deployments/docker/conf/dsiem/configs/ -type f -name 'directives_dt_*.json'| 

while read FILE ; 
do 
    newfile="$(echo ${FILE} |sed -e 's/json/txt/')" ;
    mv "${FILE}" "${newfile}" ; done 
    
