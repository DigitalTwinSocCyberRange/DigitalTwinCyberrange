while :; 
hping3 --icmp --flood -o 44140 10.0.0.1 &
PID=$!
sleep 0.09
kill $PID; do sleep 120 ; done
