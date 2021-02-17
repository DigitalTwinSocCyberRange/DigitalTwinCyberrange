#!/bin/bash

service openvswitch-switch start
mn -c
python run.py