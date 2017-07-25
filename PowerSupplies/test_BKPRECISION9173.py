import unittest as ut
from unittest import TestCase
from BKPRECISION9173 import BKPRECISION9173

BKIP = "142.103.235.210"

class TestBKPRECISION9173(TestCase):
    @ut.skip("need to write initialize values function before testing")
    def test_init_connection(self):
        self.fail()

    def test_set_voltage(self):
        bkp = BKPRECISION9173(BKIP)
        bkp.set_voltage(1, 5.2)
        bkp.set_voltage(2, 5.2)
        self.assertEqual(bkp.get_set_voltage(1), 5.2)
        self.assertEqual(bkp.get_set_voltage(2), 5.2)
        bkp.set_voltage(1, 6)
        bkp.set_voltage(2, 6)
        self.assertEqual(bkp.get_set_voltage(1), 6)
        self.assertEqual(bkp.get_set_voltage(2), 6)
        bkp.close()

    def test_set_current(self):
        bkp = BKPRECISION9173(BKIP)
        bkp.set_current(1, 1)
        bkp.set_current(2, 1)
        self.assertEqual(bkp.get_set_current(1), 1)
        self.assertEqual(bkp.get_set_current(2), 1)
        bkp.set_current(1, 1.5)
        bkp.set_current(2, 1.5)
        self.assertEqual(bkp.get_set_current(1), 1.5)
        self.assertEqual(bkp.get_set_current(2), 1.5)
        bkp.close()

    def test_turn_channel_on(self):
        self.fail()

    def test_turn_channel_off(self):
        self.fail()

    def test_measure_current(self):
        self.fail()

    def test_measure_voltage(self):
        self.fail()

    def test_get_set_current(self):
        self.fail()

    def test_get_set_voltage(self):
        self.fail()

    def test_ChannelError(self):
        self.fail()
