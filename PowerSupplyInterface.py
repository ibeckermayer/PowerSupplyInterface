import telnetlib
import time

# setup telnet connection with the power supply
HOST = "142.103.235.210"
PORT = "5024"
tn = telnetlib.Telnet(HOST, PORT)

# read until the first period (telnet connection causes an intro statement to print out)
# this is necessary since we will use '.' to identify the voltage and current query responses
print tn.read_until('.', 5)

# set the currents and voltages
CURRENT1 = 10.0
CURRENT2 = 10.0
VOLTAGE1 = 7.0
VOLTAGE2 = 7.0

# telnet needs some time in between each command or else it doesn't function properly
SLEEP_TIME = 0.5

tn.write("CURR "  + str(CURRENT1)+ "\r\n")
time.sleep(SLEEP_TIME)
tn.write("CURR2 " + str(CURRENT2)+ "\r\n")
time.sleep(SLEEP_TIME)
tn.write("VOLT "   + str(VOLTAGE1)+ "\r\n")
time.sleep(SLEEP_TIME)
tn.write("VOLT2 "  + str(VOLTAGE2)+ "\r\n")
time.sleep(SLEEP_TIME)



# close telnet connection
tn.close()


