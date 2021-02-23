while :; 
hping3 --icmp --faster -o 44140 10.0.0.1 -c 2000 &
#PID=$!
#sleep 0.09
#kill $PID; 
do sleep 120 ; done
