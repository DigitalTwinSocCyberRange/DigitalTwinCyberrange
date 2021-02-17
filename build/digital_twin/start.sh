#!/bin/bash

cd src
ls
service openvswitch-switch start
mn -c
rm ./logs/plc1.log
rm ./logs/plc2.log
rm ./logs/plc3.log
rm ./logs/tcpdump.log
rm ./logs/firewall.log

python init.py
screen -dmSL main python run.py
tail -f /dev/null