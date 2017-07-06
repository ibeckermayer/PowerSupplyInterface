import telnetlib
import time


class BKPRECISION9173:
    # initialize BKP connection with the proper host ip and port number, voltages and currents to 0
    def __init__(self):
        self.SLEEP_TIME = 0.5  # telnet is ancient and therefore needs some time to send messages
        self.host = "142.103.235.210"  # Set using manual control
        self.port = "5024"  # As described in user manual
        self.currentSetting1 = None
        self.voltageSetting1 = None
        self.currentSetting2 = None
        self.voltageSetting2 = None
        self.chan1status = None  # either ON or OFF
        self.chan2status = None  # either ON or OFF
        self.executing = false  #

    # initialize the connection and read until the first period
    def init_connection(self):
        self.tn = telnetlib.Telnet(self.host, self.port)
        time.sleep(self.SLEEP_TIME)

        # read until the first period (telnet connection causes an intro statement to print out)
        # this is necessary since we will use '.' to identify the voltage and current query responses
        self.tn.read_until('.', 5)
        time.sleep(self.SLEEP_TIME)

    # set voltage on channel 1 or 2
    def set_voltage(self, chan, voltage):
        if chan == 1:
            self.voltageSetting1 = voltage
            self.tn.write("VOLT " + str(self.voltageSetting1) + "\r\n")
            time.sleep(self.SLEEP_TIME)
        if chan == 2:
            self.voltageSetting2 = voltage
            self.tn.write("VOLT2 " + str(self.voltageSetting2) + "\r\n")
            time.sleep(self.SLEEP_TIME)

    # set current on channel 1 or 2
    def set_current(self, chan, current):
        if chan == 1:
            self.currentSetting1 = current
            self.tn.write("CURR " + str(self.currentSetting1) + "\r\n")
            time.sleep(self.SLEEP_TIME)
        if chan == 2:
            self.currentSetting2 = current
            self.tn.write("CURR2 " + str(self.currentSetting2) + "\r\n")
            time.sleep(self.SLEEP_TIME)

    # turn channel 1 or 2 ON
    def turn_channel_on(self, chan):
        if chan == 1:
            self.tn.write("OUT ON\r\n")
            time.sleep(self.SLEEP_TIME)
        if chan == 2:
            self.tn.write("OUT2 ON\r\n")
            time.sleep(self.SLEEP_TIME)

    # turn channel 1 or 2 OFF
    def turn_channel_off(self, chan):
        if chan == 1:
            self.tn.write("OUT OFF\r\n")
            time.sleep(self.SLEEP_TIME)
        if chan == 2:
            self.tn.write("OUT2 OFF\r\n")
            time.sleep(self.SLEEP_TIME)

    # close the telnet connection
    def close(self):
        self.tn.close()

    def measure_current(self, chan):
        """
Function to measure the current at the output of one of the channels.
Note that this is distinct from get_set_current, which checks what the
current is set to be at (rather than what its actually at).
        :param chan: int (1 or 2)
        :return: float
        """
        if chan == 1:
            self.tn.write("MEAS CURR?\r\n")
        if chan == 2:
            self.tn.write("MEAS CURR2?\r\n")

        time.sleep(self.SLEEP_TIME)

        before_decimal = self.tn.read_until(".", 5)
        after_decimal  = self.tn.read_until("\r")[0:3]

        if before_decimal[-3] == "\n": # check if it's 1 digit before the decimal
            before_decimal = before_decimal[-2]
        else:
            before_decimal = before_decimal[-3:-1]

        return float(before_decimal + "." + after_decimal)

    # TODO: measure_voltage(), get_set_current(), get_set_voltage()
    # TODO: make BKPRECISION9173 it's own .py file (look up how to import self made modules in python)
    # TODO: make a real test script, with unit tests and real ways to fail
        # for the sake of good coding style
        # for the sake of learning how to use this



if __name__ == "__main__":
    bkp = BKPRECISION9173()
    bkp.set_voltage(1, 6)
    bkp.set_voltage(2, 6)
    bkp.set_current(1, 1.5)
    bkp.set_current(2, 1.5)
    # bkp.turn_channel_on(2)
    # time.sleep(2)
    # bkp.turn_channel_off(2)
    bkp.close()
