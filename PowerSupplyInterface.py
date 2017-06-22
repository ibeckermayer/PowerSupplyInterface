import telnetlib
import time

class PowerSupplyInterface:
	# initialize PSI connection with the proper host ip and port number, voltages and currents to 0	
	def __init__(self):
		self.host = "142.103.235.210" # Set using manual control
		self.port = "5024"	      # As described in user manual
		self.current1 = None
		self.voltage1 = None		
		self.current2 = None
		self.voltage2 = None
		self.SLEEP_TIME = 0.5 # telnet is ancient and therefore needs some time to send messages
		
		#initialize connection
		self.tn = telnetlib.Telnet(self.host, self.port)
		time.sleep(self.SLEEP_TIME)
		
		# read until the first period (telnet connection causes an intro statement to print out)
		# this is necessary since we will use '.' to identify the voltage and current query responses
		self.tn.read_until('.', 5)
		time.sleep(self.SLEEP_TIME)

	# set voltage on channel 1 or 2
	def set_voltage(self, chan, voltage):
		if chan==1:
			print "channel1 voltage!"
			self.voltage1 = voltage
			self.tn.write("VOLT " + str(self.voltage1) + "\r\n")
			time.sleep(self.SLEEP_TIME)
		if chan==2:
			self.voltage2 = voltage
			self.tn.write("VOLT2 " + str(self.voltage2) + "\r\n")
			time.sleep(self.SLEEP_TIME)

	# set current on channel 1 or 2
	def set_current(self, chan, current):
		if chan==1:
			self.current1 = current
			self.tn.write("CURR " + str(self.current1) + "\r\n")
			time.sleep(self.SLEEP_TIME)
		if chan==2:
			self.current2 = current
			self.tn.write("CURR2 " + str(self.current2) + "\r\n")
			time.sleep(self.SLEEP_TIME)

	# close the telnet connection
	def close(self):
		self.tn.close()

if __name__ == "__main__":
	psi = PowerSupplyInterface()
	psi.set_voltage(1,6)
	psi.set_voltage(2,10)
	psi.set_current(1,10.2)
	psi.set_current(2,10.2)
	psi.close()

