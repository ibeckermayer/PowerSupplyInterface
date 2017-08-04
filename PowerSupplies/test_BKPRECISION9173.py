import unittest as ut
from unittest import TestCase
from BKPRECISION9173 import BKPRECISION9173

BKIP = "142.103.235.210"


class TestBKPRECISION9173(TestCase):
    # @ut.skip("need to write initialize values function before testing")
    def test_init_connection(self):
        bkp = BKPRECISION9173(BKIP)
        self.assertTrue(bkp.currentSetting1 is not None)
        self.assertTrue(bkp.voltageSetting1 is not None)
        self.assertTrue(bkp.currentSetting2 is not None)
        self.assertTrue(bkp.voltageSetting2 is not None)
        self.assertTrue(bkp.currentMeasured1 is not None)
        self.assertTrue(bkp.voltageMeasured1 is not None)
        self.assertTrue(bkp.currentMeasured2 is not None)
        self.assertTrue(bkp.voltageMeasured2 is not None)
        self.assertTrue(bkp.chan1on is not None)
        self.assertTrue(bkp.chan2on is not None)
        bkp.close()

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

    def test_turn_channel_on_and_off(self):
        bkp = BKPRECISION9173(BKIP)
        bkp.turn_channel_on(1)
        self.assertTrue(bkp.chan1on)
        bkp.turn_channel_on(2)
        self.assertTrue(bkp.chan2on)
        bkp.turn_channel_off(1)
        self.assertFalse(bkp.chan1on)
        bkp.turn_channel_off(2)
        self.assertFalse(bkp.chan2on)
        bkp.close()

    def test_measure_current(self):
        """
Only checking channel 2 since channel 1 is connected. Checked channel 1 manually
        """
        bkp = BKPRECISION9173(BKIP)
        bkp.set_current(2, 1.5)
        self.assertEqual(bkp.measure_current(2), 0)
        bkp.close()

    def test_measure_voltage(self):
        """
Only checking channel 2 since channel 1 is connected. Checked channel 1 manually
        """
        bkp = BKPRECISION9173(BKIP)
        bkp.set_voltage(2, 6)
        self.assertEqual(bkp.measure_voltage(2), 0)
        bkp.close()


if __name__ == '__main__':
    ut.main()
