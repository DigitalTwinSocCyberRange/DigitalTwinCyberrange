#!/bin/bash

cd src
ls
service openvswitch-switch start
mn -c
rm ./logs/plc1.log
ls ./logs
rm ./logs/plc2.log
ls ./logs
rm ./logs/plc3.log
ls ./logs
rm ./logs/tcpdump.log
ls ./logs
rm ./logs/firewall.log
ls ./logs
python init.py
screen -dmSL main python run.py
tail -f /dev/null