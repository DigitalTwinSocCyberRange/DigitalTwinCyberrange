hping3 --icmp --flood -o 44140 10.0.0.1 &
PID=$!
sleep 0.5
kill $PID
sleep 0.2
kill $PID