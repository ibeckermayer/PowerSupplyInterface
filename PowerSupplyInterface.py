import telnetlib
import time

class PowerSupplyInterface:
	def __init__(self):
		self.ip   = "142.103.235.210"
		self.port = "5024"
		self.tn = telnetlib.Telnet(self.ip, self.port)

# setup telnet connection with the power supply
HOST = "142.103.235.210"
PORT = "5024"
tn = telnetlib.Telnet(HOST, PORT)

# read until the first period (telnet connection causes an intro statement to print out)
# this is necessary since we will use '.' to identify the voltage and current query responses
tn.read_until('.')

# set the currents and voltages
CURRENT1 = 10.2
CURRENT2 = 10.2
VOLTAGE1 = 6.0
VOLTAGE2 = 10.0

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


