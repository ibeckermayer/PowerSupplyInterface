import telnetlib
import time
from Errors import *

class BKPRECISION9173:
    def __init__(self, host):
        """
initialize BKP connection with the proper host ip and port number
        :param host: string with ip address of the device
        """
        self.SLEEP_TIME = 1  # telnet is ancient and therefore needs some time to send messages
        self.host = host  # Set using manual control
        self.port = "5024"  # As described in user manual
        self.currentSetting1 = None
        self.voltageSetting1 = None
        self.currentSetting2 = None
        self.voltageSetting2 = None
        self.currentMeasured1 = None
        self.voltageMeasured1 = None
        self.currentMeasured2 = None
        self.voltageMeasured2 = None
        self.chan1on = None  # either True or False
        self.chan2on = None  # either True or False
        self.executing = False  # may be necessary later to avoid data acquisition / command overlap
        self.init_connection()
        self.read_all_vals()

    def read_all_vals(self):
        """
function to read all the values from the BKP and set the fields upon a new connection
        """
        self.currentSetting1 = self.get_set_current(1)
        self.currentSetting2 = self.get_set_current(2)
        self.voltageSetting1 = self.get_set_voltage(1)
        self.voltageSetting2 = self.get_set_voltage(2)
        self.currentMeasured1 = self.measure_current(1)
        self.currentMeasured2 = self.measure_current(2)
        self.voltageMeasured1 = self.measure_voltage(1)
        self.voltageMeasured2 = self.measure_voltage(2)
        self.chan1on = self.is_chan_on(1)
        self.chan2on = self.is_chan_on(2)

    def is_chan_on(self, chan):
        """
check if the channel is on
        :param chan: int (1 or 2)
        :return: boolean
        """
        if chan == 1:
            self.send_command("OUT?")
        elif chan == 2:
            self.send_command("OUT2?")
        else:
            raise ChannelError(chan)

        onOrOff = self.read_on_or_off()
        if onOrOff == "ON":
            return True
        elif onOrOff == "OFF":
            return False

    def read_on_or_off(self):
        self.read_until("O")
        string2check = self.read_until("\r")
        if string2check[0] == "N":
            return "ON"
        elif string2check[0] == "F":
            return "OFF"

    def init_connection(self):
        """
initialize the telnet connection
        """
        self.tn = telnetlib.Telnet(self.host, self.port)
        time.sleep(self.SLEEP_TIME)

        # read until the first period (telnet connection causes an intro statement to print out)
        # this is necessary since we will use '.' to identify the voltage and current query responses
        self.read_until('.')

    def send_command(self, command):
        """
function for sending commands via telnet connection
        :param command: string
        """
        self.tn.write(command + "\r\n")  # always need "\r\n" at the end to actually send
        time.sleep(self.SLEEP_TIME)  # always want to sleep after to ensure command has time to be received

    def read_until(self, string):
        """
Function for reading back until a given string, returns everything read back
        :param string: string
        :return: string
        """
        return_string = self.tn.read_until(string, 5)
        time.sleep(self.SLEEP_TIME)  # always sleep after to make sure timing is ok
        return return_string

    def set_voltage(self, chan, voltage):
        """
set voltage on channel 1 or 2
        :param chan: int (1 or 2)
        :param voltage: float or int
        """
        if chan == 1:
            self.voltageSetting1 = voltage
            self.send_command("VOLT " + str(self.voltageSetting1))
        elif chan == 2:
            self.voltageSetting2 = voltage
            self.send_command("VOLT2 " + str(self.voltageSetting2))
        else:
            raise ChannelError(chan)

    def set_current(self, chan, current):
        """
set current on channel 1 or 2
        :param chan: int (1 or 2)
        :param current: float or int
        """
        if chan == 1:
            self.currentSetting1 = current
            self.send_command("CURR " + str(self.currentSetting1))
        elif chan == 2:
            self.currentSetting2 = current
            self.send_command("CURR2 " + str(self.currentSetting2))
        else:
            raise ChannelError(chan)

    def turn_channel_on(self, chan):
        """
turn channel 1 or 2 ON
        :param chan: int (1 or 2)
        """
        if chan == 1:
            self.send_command("OUT ON")
        elif chan == 2:
            self.send_command("OUT2 ON")
        else:
            raise ChannelError(chan)

    def turn_channel_off(self, chan):
        """
turn channel 1 or 2 OFF
        :param chan: int (1 or 2)
        """
        if chan == 1:
            self.send_command("OUT OFF")
        elif chan == 2:
            self.send_command("OUT2 OFF")
        else:
            raise ChannelError(chan)

    def close(self):
        """
close the telnet connection
        """
        self.tn.close()

    def extract_float_readback(self):
        """
After asking for a measurement from the system, extract the readout with this algorithm
        :return: float
        """
        before_decimal = self.read_until(".")
        print "before _decimal = " + before_decimal #debug
        after_decimal = self.read_until("\r")[0:3]
        if before_decimal[-3] == "\n":  # check if it's 1 digit before the decimal
            before_decimal = before_decimal[-2]
        else:
            before_decimal = before_decimal[-3:-1]
        return float(before_decimal + "." + after_decimal)

    def measure_current(self, chan):
        """
Function to measure the current at the output of one of the channels.
Note that this is distinct from get_set_current, which checks what the
current is set to be at (rather than what its actually at).
        :param chan: int (1 or 2)
        :return: float
        """
        if chan == 1:
            self.send_command("MEAS CURR?")
        elif chan == 2:
            self.send_command("MEAS CURR2?")
        else:
            raise ChannelError(chan)
        return self.extract_float_readback()

    def measure_voltage(self, chan):
        """
Function to measure the voltage at the output of one of the channels.
Note that this is distinct from get_set_voltage, which checks what the
voltage is set to be at (rather than what its actually at).
        :param chan: int (1 or 2)
        :return: float
        """
        if chan == 1:
            self.send_command("MEAS VOLT?")
        elif chan == 2:
            self.send_command("MEAS VOLT2?")
        else:
            raise ChannelError(chan)
        return self.extract_float_readback()

    def get_set_current(self, chan):
        """
Function to get the current the machine is set to run at
        :param chan: int (1 or 2)
        :return: float
        """
        if chan == 1:
            self.send_command("CURR?")
        elif chan == 2:
            self.send_command("CURR2?")
        else:
            raise ChannelError(chan)
        return self.extract_float_readback()

    def get_set_voltage(self, chan):
        """
Function to get the voltage the machine is set to run at
        :param chan: int (1 or 2)
        :return: float
        """
        if chan == 1:
            self.send_command("VOLT?")
        elif chan == 2:
            self.send_command("VOLT2?")
        else:
            raise ChannelError(chan)
        return self.extract_float_readback()

        # for the sake of good coding style
        # for the sake of learning how to use this
        # TODO: make a function to test if channels are on or not
        # TODO: make some functions for initialization, which measure and set the fields
        # TODO: choose which fields you want to have, add them to initialization and to the test functions
        # I want a measured current and voltage field as well as a set current and voltage field
        # I want to initialize the class with the IP address
        # When I change the current or the voltage, I want to measure the set current/voltage (and make the set volt/curr = to this)
        # If what I set and what I read is different, I want to throw an error that says the voltage/current was not set properly
        # TODO: add errors for bad channel numbers and bad curr/volt values, and test these errors
