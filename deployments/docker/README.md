# SIEM configuration

To connect Dsiem with the digital twin simulation the following configuration files were adapted as described [here](https://github.com/defenxor/dsiem/blob/master/docs/event_processing.md).

Parse logs from the src/logs directory:

[filebeat.yml](https://github.com/lenaglas/DigitalTwinCyberrange/blob/main/deployments/docker/conf/filebeat/filebeat.yml)



Normalize logs to SIEM Events and create digital-twin Index for elasticsearch:

[40_digitaltwin-pipeline.conf](https://github.com/lenaglas/DigitalTwinCyberrange/blob/main/deployments/docker/conf/logstash/conf.d/40_digitaltwin-pipeline.conf)

[70_dsiem-plugin_digital_twin.conf](https://github.com/lenaglas/DigitalTwinCyberrange/blob/main/deployments/docker/conf/logstash/conf.d/70_dsiem-plugin_digital_twin.conf)

[99_output.conf](https://github.com/lenaglas/DigitalTwinCyberrange/blob/main/deployments/docker/conf/logstash/conf.d/99_output.conf)



 The json correlation directives are stored in the [configs](https://github.com/lenaglas/DigitalTwinCyberrange/tree/main/deployments/docker/conf/dsiem/configs) directory of Dsiem. 
