docker-compose -f create-certs.yml run --rm create_certs
docker-compose up -d es01
until $(docker run --rm -v es_certs:/certs --network=es_default docker.elastic.co/elasticsearch/elasticsearch:7.6.0 curl --output /dev/null --silent --fail --cacert /certs/ca/ca.crt -u elastic:PleaseChangeMe https://es01:9200)
do
    echo "Elasticsearch not started yet - sleeping"
    sleep 2
done
echo "Elasticsearch running"
docker exec -it es01 /bin/bash -c "bin/elasticsearch-setup-passwords interactive --url https://localhost:9200"
docker-compose down