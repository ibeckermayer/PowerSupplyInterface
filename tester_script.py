# Script for testing telnet readback to write proper functions for data aquisition
import telnetlib
import time
host = "142.103.235.210"
port = "5024"
SLEEP_TIME = 0.5

tn = telnetlib.Telnet(host, port)
time.sleep(SLEEP_TIME)
tn.read_until('.', 5)
time.sleep(SLEEP_TIME)
